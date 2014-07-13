# A subscription will belong to more than one state.

# Subscriptions that are valid for the current time.
# This includes subscriptions in a trial period
SUBSCRIPTION_STATE_ACTIVE = "active"
# Subscriptions that are valid for the current time but
# will not renew because a cancelation was requested
SUBSCRIPTION_STATE_CANCELED = "canceled"
# Subscriptions that have expired and are no longer valid
SUBSCRIPTION_STATE_EXPIRED = "expired"
# Subscriptions that will start in the future, they are not active yet
SUBSCRIPTION_STATE_FUTURE = "future"
# Subscriptions that are active or canceled and are in a trial period
SUBSCRIPTION_STATE_IN_TRIAL = "in_trial"
# All subscriptions that are not expired
SUBSCRIPTION_STATE_LIVE = "live"
# Subscriptions that are active or canceled and have a past-due invoice
SUBSCRIPTION_STATE_PAST_DUE = "past_due"
