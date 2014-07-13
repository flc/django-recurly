# https://docs.recurly.com/api/push-notifications
# https://docs.recurly.com/push-notifications
# IMPORTANT!
# Webhooks are not actionable on their own and should not be used for critical functions
# like provisioning accounts. Use the receipt of a webhook to trigger an API query to
# validate the push notification details against the current API data.

from django.dispatch import Signal


# Account Notifications

# New Account
# Sent when a new account is created.
new_account_notification = Signal(providing_args=('data',))
# Closed Account
# Sent when an account is closed.
canceled_account_notification = Signal(providing_args=('data',))
# Updated Billing Information
# Sent when billing information is successfully created or updated on an account.
billing_info_updated_notification = Signal(providing_args=('data',))
# Reactivated Account
# Sent when an account subscription is reactivated after having been canceled.
reactivated_account_notification = Signal(providing_args=('data',))


# Invoices

# New Invoice, New Invoice (Manual)
# If a new invoice is generated, a new_invoice_notification is sent.
new_invoice_notification = Signal(providing_args=('data',))
# Closed Invoice, Closed Invoice (Manual)
closed_invoice_notification = Signal(providing_args=('data',))
# Past Due Invoice, Past Due Invoice (Manual)
past_due_invoice_notification = Signal(providing_args=('data',))


# Subscription Notifications

# New Subscription
# Sent when a new subscription is created.
new_subscription_notification = Signal(providing_args=('data',))
# Updated Subscription
# When a subscription is upgraded or downgraded, Recurly will send an
# updated_subscription_notification. The notification is sent after the
# modification is performed. If you modify a subscription and it takes place
# immediately, the notification will also be sent immediately. If the
# subscription change takes effect at renewal, then the notification will be
# sent when the subscription renews. Therefore, if you receive an
# updated_subscription_notification, it contains the latest subscription information.
updated_subscription_notification = Signal(providing_args=('data',))
# Canceled Subscription
# The canceled_subscription_notification is sent when a subscription is canceled.
# This means the subscription will not renew. The subscription state is set to
# canceled but the subscription is still valid until the expires_at date.
# The next notification is sent when the subscription is completely terminated.
canceled_subscription_notification = Signal(providing_args=('data',))
# Expired Subscription
# The expired_subscription_notification is sent when a subscription is no longer valid.
# This can happen if a canceled subscription expires or if an active subscription is refunded
# (and terminated immediately). If you receive this message, the account no longer has a subscription.
expired_subscription_notification = Signal(providing_args=('data',))
# Renewed Subscription
# The renewed_subscription_notification is sent whenever a subscription renews.
# This notification is sent regardless of a successful payment being applied to the
# subscription-it indicates the previous term is over and the subscription is now in a new term.
# If you are performing metered or usage-based billing, use this notification to reset your
# usage stats for the current billing term.
renewed_subscription_notification = Signal(providing_args=('data',))


# Payments

# Successful Payment, Manual Payment
# A successful_payment_notification is sent when a payment is successfully captured.
# A successful_payment_notification is also sent when a manual offline payment is recorded.
successful_payment_notification = Signal(providing_args=('data',))
# Failed Payment
# A failed_payment_notification is sent when a payment attempt is declined
# by the payment gateway.
failed_payment_notification = Signal(providing_args=('data',))
# Successful Refund
# If you refund an amount through the API or admin interface, a successful_refund_notification
# is sent. Failed refund attempts do not generate a notification.
successful_refund_notification = Signal(providing_args=('data',))
# Void Payment
# If you void a successfully captured payment before it settles, a void_payment_notification
# is sent. Payments can only be voided before the funds settle into your merchant account.
void_payment_notification = Signal(providing_args=('data',))
