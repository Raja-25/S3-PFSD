import random


class Train:
    tid = 18046
    tname = "east coast express"
    size = 30
    time = 17.30
    source = "Hyd"
    Destination = "Shalimar"


class Book(Train):
    n = int(input("enter no of tickets"))
    if n > Train.size:
        print("not enough seats")
        quit()
    ticketnum = random.sample(range(1, 30), n)


d = Book()
print("Ticket Details")
print("Ticket id=",random.randint(100000,999999))
print("train number=", d.tid)
print("train Name=", d.tname)
print("train Source=", d.source)
print("train Destination=", d.Destination)
print("Seat numbers are=", d.ticketnum)
