""" Dweet Storage """
import requests

from store import StateStorage

DWEET = "your-thing-here"
DWEET_GET = f"https://dweet.io/get/latest/dweet/for/{DWEET}"
DWEET_POST = f"https://dweet.io/dweet/for/{DWEET}"


class DweetStateStorage(StateStorage):
    def get_state(self):
        """ Dweet Magic """
        try:
            return requests.get(DWEET_GET).json()['with'][0]['content']
        except TypeError:
            self.store_state({})
            return {}

    
    def store_state(self, state: dict):
        """ Dweet Big Magic """
        requests.post(DWEET_POST, json=state)
        return 0


EXPORTS = {
    'type':'store',
    'store':DweetStateStorage()
}

if __name__ == "__main__":
    DweetStateStorage().store_state({})
