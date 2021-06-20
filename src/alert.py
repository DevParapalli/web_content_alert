from requests import post
from time import sleep

class BaseAlertProvider:

    def execute(self, title, message) -> bool:
        try:
            print(f"[ALERT]\nTitle:{title}\nMessage:{message}")
            return True
        except Exception as _:
            return False


class DiscordWebhookAlertProvider(BaseAlertProvider):
    # TODO: Maybe think about creating a Embeded message too
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
        sleep(1) # TODO: Figure out how to remove this. (Stops X-ratelimit-limit == 0)
        resp = post(
            url=self.webhook,
            json={"content": self.DISCORD_MESSAGE.format(
                title=title.upper(),
                message=message
            )}
        )
        debug_headers = {}
        debug_headers['x-ratelimit-bucket'] =resp.headers.get('x-ratelimit-bucket', "not-found")
        debug_headers['x-ratelimit-limit'] =resp.headers.get('x-ratelimit-limit', "not-found")
        debug_headers['x-ratelimit-ramaining'] =resp.headers.get('x-ratelimit-remaining', "not-found")
        debug_headers['x-ratelimit-reset'] =resp.headers.get('x-ratelimit-reset', "not-found")
        debug_headers['x-ratelimit-resetafter'] =resp.headers.get('x-ratelimit-resetafter', "not-found")
        # TODO: Create a client sided rate limiter 
        print(f"{resp.status_code=}, {debug_headers=}")
        


if __name__ == "__main__":
    # Testing for discord webhooks
    print("I don't know why this works.")
