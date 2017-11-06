
class Person():
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address

    def getName(self):
        return self.name
    def getAddress(self):
        return self.address

    def __str__(self):
        n = self.getName()
        a = self.getAddress()
        output = "Person[name={},address={}]"
        return output.format(n,a)
        #str1 = str("Person[name=" + n)         #\
        #str2 = str("address=" + a + "]")       # Just another (ugly) way of doing it..
        #return str1 + "," + str2               #/
