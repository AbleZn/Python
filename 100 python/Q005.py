# Q005
# Created by JKChang
# 17/02/2017, 09:00
# Tag: class
# # Description: Define a class which has at least two methods:
#                getString: to get a string from console input # printString: to print the string in upper case.
#                Also please include simple test function to test the class methods.

class InputOutputString(object):
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input('input: ')

    def printString(self):
        print(self.s.upper())

test = InputOutputString()
test.getString()
test.printString()
