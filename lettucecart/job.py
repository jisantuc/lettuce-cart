"""Base Job class
"""

class Job(object):

    def __init__(self):
        pass

    def start(self):
        pass

    def complete(self):
        self.notify()
        pass

    def notify(self):
        pass
