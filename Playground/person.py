
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
        str1 = "Person[name=" + n
        str2 = "address=" + a + "]"
        return str1 + "," + str2
