class RequestProcessor:
    required_input_keys = [] #keys that request payload has to contain

    def __init__(self, request, database):
        self.request = request
        self.database = database

    def process(self):
        pass

    def _verify_payload(self, payload):
        if not payload:
            return BAD_REQUEST_ERROR_MESSAGE

        for key in required_input_keys:
            if not key in payload.keys():
                return BAD_REQUEST_ERROR_MESSAGE

        for key in required_input_keys:
            if not payload[key]:
                return BAD_REQUEST_ERROR_MESSAGE

    
