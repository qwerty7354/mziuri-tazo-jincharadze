class Ticket:
    def __init__(self, film_name, time, hall, row, seat, price=10):
        self.film_name = film_name
        self.time = time
        self.hall = hall
        self.row = row
        self.seat = seat
        self.price = price

    def __str__(self):
        return f"pilmi: {self.film_name}, dro: {self.time}, darbazi: {self.hall}, rigi: {self.row}, adgili: {self.seat}, fasi: {self.price}$"

class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.tickets = []

    def __str__(self):
        return f"momxmarebeli:{self.name}, balanci:{self.balance}$"

    def deposit(self, amount):
        self.balance += amount
        print(f"balanci sheivso {amount} $-it axali balansi: {self.balance}")

    def buy_ticket(self, ticket):
        if self.balance >= ticket.price:
            self.balance -= ticket.price
            self.tickets.append(ticket)
            print("bileti iyide!")
        else:
            print("puli ar gaq ra bileti ginda?")

    def show_tickets(self):
        if not self.tickets:
            print("bileti ar gaq")
        else:
            print("tqveni biletebi: ")
            for t in self.tickets:
                print(t)


ticket1 = Ticket("Inception", "18:00", "A", row=5, seat=12)
ticket2 = Ticket("Interstellar", "20:30", "B", row=3, seat=7)

user = User("Jasurbek Iaxshibovichi", balance=0)

user.deposit(25)

user.buy_ticket(ticket1)
user.buy_ticket(ticket2)

user.show_tickets()

print(user)
