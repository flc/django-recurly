import logging
import recurly

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from shortuuidfield import ShortUUIDField

from . import settings as app_settings
from .utils import (
    get_hosted_account_management_url,
    get_hosted_payment_page_url,
    )


recurly.SUBDOMAIN = app_settings.RECURLY_SUBDOMAIN
recurly.API_KEY = app_settings.RECURLY_API_PRIVATE_KEY
recurly.DEFAULT_CURRENCY = app_settings.RECURLY_DEFAULT_CURRENCY


logger = logging.getLogger(__name__)


class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="recurly_account",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        )
    account_code = ShortUUIDField(
        unique=True,
        db_index=True,
        )
    # store this for caching purposes
    hosted_login_token = models.TextField(blank=True)

    def get_hosted_account_management_url(self):
        if not self.hosted_login_token:
            return None
        return get_hosted_account_management_url(self.hosted_login_token)

    def get_hosted_payment_page_url_params(self):
        data = {
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email,
            'username': getattr(self.user, "username", None),
        }
        return data

    def get_hosted_payment_page_url(self, plan_code):
        data = self.get_hosted_payment_page_url_params()
        return get_hosted_payment_page_url(plan_code, self.account_code, data)

    @classmethod
    def get_or_create_from_user(cls, user):
        obj, created = cls.objects.get_or_create(user=user)
        return obj, created

    def fetch_from_api(self):
        return recurly.Account.get(self.account_code)
