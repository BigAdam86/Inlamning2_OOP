from person import Person

class Student(Person):
    def __init(self,name,address):
        super().__init__(name,address)

    def set_name(self, name):
        super().set_name(name)
    def set_address(self, address):
        super().set_address(address)

    def get_name(self):
        super().get_name()
    def get_address(self):
        super().get_address()
