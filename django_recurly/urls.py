from django.conf.urls import patterns, url, include

from . import views


urlpatterns = patterns("",
    url(r"^notification/$", views.push_notification, name="notification"),
    # url(r"^success/$", success_token, name="success_url"),
    # url(r"^change-plan/$", change_plan, name="change_plan"),
    # url(r"^account/$", account, name="account"),
    # url(r"^invoice/(?P<uuid>[a-z0-9]+)\.pdf$", invoice, name="invoice"),
)
