from util import BASE_DIR
from json import dumps, loads

class StateStorage:
    def get_state(self):
        "Does some magic and gets the previous data stored"
        with open(BASE_DIR.parent / 'state.json') as f:
            state:dict = loads(f.read())
        return state
    
    def store_state(self, state:dict):
        "Does even more magic and saves the state"
        with open(BASE_DIR.parent / 'state.json', "w") as f:
            byte = f.write(dumps(state))
        return byte


if __name__ == "__main__":
    StateStorage().store_state({})