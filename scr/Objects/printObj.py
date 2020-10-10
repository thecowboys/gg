
class PrintObject(object):

    def __init__(self):
        self.exec_string = ""

    def transpile(self, value):
        self.exec_string += value
        return self.exec_string
