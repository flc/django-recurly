import logging

import recurly

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .decorators import recurly_basic_authentication
from . import signals
from .models import Account


logger = logging.getLogger(__name__)


@csrf_exempt
@recurly_basic_authentication
@require_POST
def push_notification(request):
    # big try catch because we don't want to send recurly any
    # technical error response with all our settings if we happen to
    # test the webhooks with DEBUG=True
    try:
        data = recurly.objects_for_push_notification(request.body)

        try:
            _type = data['type']
            logger.info("Recurly notification: %s", _type)
            signal = getattr(signals, _type)
        except AttributeError:
            return HttpResponseBadRequest("Unrecognized notification type.")

        signal.send(sender=request, data=data)
    except Exception as e:
        if settings.DEBUG:
            logger.exception(e)
            return HttpResponse(status=500)
        raise

    return HttpResponse()


if 'rest_framework' in settings.INSTALLED_APPS:
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import authentication, permissions
    from rest_framework import status


    class HostedPaymentPageData(APIView):
        allowed_methods = ['post']

        permission_classes = (permissions.IsAuthenticated, )

        def post(self, request, format=None):
            # we use POST because it's possible that there is no
            # associated Account object for the user yet and we
            # need to create it and generate a unique account_code
            # for it
            try:
                plan_code = request.DATA['plan_code']
            except KeyError:
                return Response(
                    {'plan_code': 'Plan code is missing'},
                    status=status.HTTP_400_BAD_REQUEST,
                    )

            user = request.user
            account, created = Account.get_or_create_from_user(user)
            return Response({
                'url': account.get_hosted_payment_page_url(plan_code)
                })


    class HostedAccountManagementPageData(APIView):

        def get(self, request, format=None):
            user = request.user
            try:
                account = Account.objects.filter(user=request.user)[0]
            except IndexError:
                url = None
            else:
                url = account.get_hosted_account_management_url()
            return Response({
                'url': url
                })

