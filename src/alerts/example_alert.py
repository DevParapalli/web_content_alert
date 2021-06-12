from ..alert import DiscordWebhookAlertProvider

# Alert config
alert = DiscordWebhookAlertProvider(
    "<webhook_url>"
)

EXPORTS = {
    'type':"alerts",
    'alert-function':alert
}