#N1

class BankAccount:
    MAX_DEPOSIT = 2500

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("tanxa unda iyos dadebiti.")
        elif amount > self.MAX_DEPOSIT:
            print(f"sheudzlebelia {self.MAX_DEPOSIT}₾-ze metis shetana ertdroulad.")
        else:
            self.balance += amount
            print(f"shetanilia {amount}₾. axali balansi: {self.balance}₾")

    def withdraw(self, amount):
        if amount <= 0:
            print("tanxa unda iyos dadebiti.")
        elif amount > self.balance:
            print(f"arasakmarisi tanxa. tkveni balansia: {self.balance}₾")
        else:
            self.balance -= amount
            print(f"gamotanilia {amount}₾. axali balansi: {self.balance}₾")

    def display_balance(self):
        print(f"mflobeli: {self.owner} | balansi: {self.balance}₾")

#N2

import math

class Shape:
    def describe(self):
        print("I am a shape")


class Polygon(Shape):
    def __init__(self, *sides):
        self.sides = sides

    def describe(self):
        super().describe()
        print(f"maqvs {len(self.sides)} gverdi: {self.sides}")


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return round(area, 2)

