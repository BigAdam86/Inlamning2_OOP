from person import Person

class Student(Person):
    def __init__(self,name,address,program,year,fee):
        super().__init__(name,address)
        self.program = str(program)
        self.year = int(year)
        self.fee = float(fee)

    def setName(self, name):
        super().setName(name)
    def setAddress(self, address):
        super().setAddress(address)
    def setProgram(self,program):
        self.program = program
    def setYear(self, year=2017):
        self.year = year
    def setFee(self, fee):
        self.fee = fee

    def getName(self):
        return super().getName()
    def getAddress(self):
        return super().getAddress()
    def getProgram(self):
        return self.program
    def getYear(self):
        return self.year
    def getFee(self):
        return self.fee

    def __str__(self):
        p = self.getProgram()
        y = self.getYear()
        f = "%.2f" % self.getFee()
        output = "Student[{},program={},year={},fee={}]"
        returnVal = output.format(super().__str__(), p,y,f)
        return returnVal
