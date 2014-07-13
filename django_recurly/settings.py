from django.conf import settings


RECURLY_SUBDOMAIN = settings.RECURLY_SUBDOMAIN
RECURLY_API_PRIVATE_KEY = settings.RECURLY_API_PRIVATE_KEY
RECURLY_API_PUBLIC_KEY = getattr(settings, "RECURLY_API_PUBLIC_KEY", None)
RECURLY_JS_PRIVATE_KEY = getattr(settings, "RECURLY_JS_PRIVATE_KEY", None)
RECURLY_DEFAULT_CURRENCY = getattr(
    settings, "RECURLY_DEFAULT_CURRENCY",
    getattr(settings, "SITE_CURRENCY", "USD")
    )
# The username & password used to authorise Recurly's
# webhook. In the format "username:password"
RECURLY_WEBHOOK_HTTP_AUTHENTICATION = \
    getattr(settings, 'RECURLY_WEBHOOK_HTTP_AUTHENTICATION', None)
