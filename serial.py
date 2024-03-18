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
    def __init__ (self, start=0):
        self.start = start
        self.next_serial = start
        
    def generate(self):
        """ takes serial and add one each time around then returns the number"""
        serial = self.next_serial
        self.next_serial += 1
        return serial
    
    def reset(self):
        """ resets the "counter" to the origanl start number"""
        self.next_serial = self.start

serial = SerialGenerator(start=100)

print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())