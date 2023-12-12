class StatusError(Exception):
    def __init__(self, msg):
        self.arg = msg

class FetchPageError(Exception):
    def __init__(self, msg):
        self.arg = msg


