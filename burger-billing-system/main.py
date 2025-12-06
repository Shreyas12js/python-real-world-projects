print("Welcome to the Burger Shop!")

size = input("Enter burger size (S for Small, M for Medium, L for Large): ").upper()
add_mushroom = input("Add mushroom? (Y/N): ").upper()
extra_cheese = input("Add extra cheese? (Y/N): ").upper()

bill = 0

# Base prices
if size == "S":
    bill += 5
elif size == "M":
    bill += 8
elif size == "L":
    bill += 10
else:
    print("Invalid size entered!")
    exit()

# Mushroom pricing
if add_mushroom == "Y":
    bill += 2 if size == "L" else 1

# Extra cheese
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
print("**** Thank you! Please visit again! ****")

