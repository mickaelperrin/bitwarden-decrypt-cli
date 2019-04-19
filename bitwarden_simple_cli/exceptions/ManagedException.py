
class ManagedException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class ProperExit(Exception):
    def __init__(self, *args, message='', **kwargs) :
        Exception.__init__(self, *args, **kwargs)