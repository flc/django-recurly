import functools

from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.utils.crypto import constant_time_compare

from . import settings as app_settings


def recurly_basic_authentication(fn):
    @functools.wraps(fn)
    def wrapper(request, *args, **kwargs):
        authentication = app_settings.RECURLY_WEBHOOK_HTTP_AUTHENTICATION

        # If the user has not setup settings.RECURLY_WEBHOOK_HTTP_AUTHENTICATION then
        # we trust they are doing it at the web server level.
        if authentication is None:
            return fn(request, *args, **kwargs)

        try:
            method, auth = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
        except KeyError:
            response = HttpResponse()
            response.status_code = 401
            response['WWW-Authenticate'] = 'Basic realm="Restricted"'
            return response

        try:
            if method.lower() != 'basic':
                raise ValueError()

            if not constant_time_compare(auth.strip().decode('base64'), authentication):
                return HttpResponseForbidden()
        except Exception:
            return HttpResponseBadRequest()

        return fn(request, *args, **kwargs)
    return wrapper
