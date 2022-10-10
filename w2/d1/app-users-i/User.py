class User:

    def __init__(self, name, email, address, drivers_license):
        self.name = name
        self.email = email
        self.address = address
        self.drivers_license = drivers_license

    def __str__(self):
        return f'name: {self.name}\nemail: {self.email}\naddress: {self.address}\ndrivers license: {self.drivers_license}'


fifo = User('Fifo', 'fifo99@gmail.com', '123 fake street', '1234123412311')
print(fifo)