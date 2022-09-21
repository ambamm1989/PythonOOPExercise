"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

def _init_(self, start = 0):

    self.start = self.next = start

def _repr_(self):

    return 

def generat(self):
    self.next += 1
    return self.next - 1

def reset(self):
    self.next = self.start