class Person:
    def __init__(self, name, phones):
        self.name = name
        self.phones = phones
    def __str__(self):
        str = f'name: {self.name}'
        for p in phones:
            str += f'\n\tnumber: {p.number}'
        return str

class Phone:
    def __init__(self, number):
        self.number = number
    def __str__(self):
        return self.number

phones = [Phone('1234'), Phone('9876')]
p = Person("Bilbo", phones)
print(p)
