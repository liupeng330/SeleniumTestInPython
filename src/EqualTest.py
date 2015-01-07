class EqualTest(object):
    def __init__(self, name):
        self.name = name 
        
    # overrid ==
    def __eq__(self, other):
        return (isinstance(other, self.__class__)) and self.name == other.name
    
    # overrid !=
    def __ne__(self, other):
        return not self.__eq__(other)

if __name__ == "__main__":
    a = EqualTest('Peng')
    b = EqualTest('Liu')
    print a == b
    print a != b
