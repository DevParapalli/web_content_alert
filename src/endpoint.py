
class Endpoint():
    def __init__(self, function_get, function_process, context:dict):
        self._get = function_get
        self._proc = function_process
        self._context = context
        self._raw_data = self._get(self._context)
    
    def get_data(self):
        return self._proc(self._raw_data, self._context)
    
