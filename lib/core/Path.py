class Path(object):
    def __init__(self, path=None, status=None, response=None):
        self.path = path
        self.status = status
        self.response = response

    def __str__(self):
        return self.path

    def __del__(self):
        del(self.status)
        del(self.response)
        del(self.path)