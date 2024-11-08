class Flight():
    def __init__(self, capacity):   #Method to create a new flight
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):  #Method to add a passenger
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):                                   #Method to check if a flight has open seats
        return self.capacity - len(self.passengers)

flight = Flight(3)  

travelers = ["Orie", "Tumzie", "BieKay", "Moolzar"]
for person in travelers:
    loaded = flight.add_passenger(person)
    if loaded:
        print(f"boarded {person} to flight successfully.")
    else:
        print(f"No available seats for {person}, please try the next flight.")
