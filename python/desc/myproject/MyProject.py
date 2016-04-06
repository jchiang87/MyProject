__all__ = ['MyProject']

class MyProject(object):
    '''
    Example class for MyProject package.
    '''
    def __init__(self, message):
        self.message = message

    def run(self, raise_error=False):
        if raise_error:
            raise RuntimeError()
        return self.message
