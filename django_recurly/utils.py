import urllib
import urlparse

from . import settings as app_settings


def get_hosted_account_management_url(hosted_login_token):
    return 'https://%s.recurly.com/account/%s' % (
        app_settings.RECURLY_SUBDOMAIN,
        hosted_login_token,
    )


def encode_dict(data):
    return dict([
        (key, val.encode('utf-8')) for key, val in data.items()
        if isinstance(val, basestring)
        ])


def get_hosted_payment_page_url(plan_code, account_code, data=None):
    if not data:
        data = {}

    # passing account_code and username as a query param would also work
    # data['account_code'] = account_code
    # url = 'https://%s.recurly.com/subscribe/%s/%s' % (
    #     app_settings.RECURLY_SUBDOMAIN,
    #     plan_code,
    #     urllib.urlencode(encode_dict(data))
    # )
    url = 'https://%s.recurly.com/subscribe/%s/%s/' % (
        app_settings.RECURLY_SUBDOMAIN,
        plan_code,
        account_code,
    )
    username = data.pop("username", None)
    if username:
        url = urlparse.urljoin(url, username)
    return '%s?%s' % (
        url,
        urllib.urlencode(encode_dict(data)),
    )
