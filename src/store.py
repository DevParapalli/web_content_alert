from util import BASE_DIR
from json import dumps, loads

class StateStorage:
    def get_state(self):
        "Simple Filesystem Store"
        with open(BASE_DIR.parent / 'state.json') as f:
            state:dict = loads(f.read())
        return state
    
    def store_state(self, state:dict):
        "Simple FileSystem Store"
        with open(BASE_DIR.parent / 'state.json', "w") as f:
            byte = f.write(dumps(state))
        return byte


if __name__ == "__main__":
    StateStorage().store_state({})