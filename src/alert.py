from requests import post


class BaseAlertProvider:

    def execute(self, title, message) -> bool:
        try:
            print(f"[ALERT]\nTitle:{title}\nMessage:{message}")
            return True
        except Exception as _:
            return False


class DiscordWebhookAlertProvider(BaseAlertProvider):

    DISCORD_MESSAGE = """
```
[{title}]
{message}
```
"""

    def __init__(self, webhook: str) -> None:
        self.webhook = webhook

    def execute(self, title:str, message:str) -> bool:
        super().execute(title, message)
        post(
            url=self.webhook,
            json={"content": self.DISCORD_MESSAGE.format(
                title=title.upper(),
                message=message
            )}
        )


if __name__ == "__main__":
    # Testing for discord webhooks
    print("I don't know why this works.")