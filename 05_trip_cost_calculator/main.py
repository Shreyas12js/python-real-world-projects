print("Welcome to the Trip Cost Calculator!")

days = int(input("How many days will you stay? "))
hotel = float(input("How much does hotel cost per night? $"))
flight = float(input("How much does flight cost? $"))
car = float(input("If you need rental car please enter the price otherwise enter zero. $"))
other = float(input("Enter other possible expenses $"))

hotel_total = hotel * days
car_total = car * days

total_cost = round(hotel_total + flight + car_total + other , 2)

print(f"Total Cost: ${total_cost}")
