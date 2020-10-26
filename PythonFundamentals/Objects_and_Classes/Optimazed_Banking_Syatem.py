class BankAccount:
    def __init__(self, bank, name, balance):
        self.__bank = bank
        self.__name = name
        self.__balance = balance

    def get_name(self):
        return self.__name
    def get_bank(self):
        return self.__bank
    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f'{self.get_name()} {self.get_bank()} {self.get_balance()}'

storage = []

while True:
    string = input()
    if string == 'end':
        break
    string2 = string.split(' | ')
    storage.append(string2)
storage2 = []
for n in range(0, len(storage)):
    a = BankAccount(storage[n][0], storage[n][1], float(storage[n][2]))
    storage2.append(a)
b =  sorted(storage2, key=lambda x: (-x.get_balance(), x.get_bank()))
for c in b:
    print(f'{c.get_name()} -> {c.get_balance():.2f} ({c.get_bank()})')








