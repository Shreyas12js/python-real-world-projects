hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours <= 40:
    pay = hours * rate
else:
    overtime = hours - 40
    pay = (40 * rate) + (overtime * rate * 1.5)
    final_pay = round(pay , 2)

print(f"Pay: {final_pay}")
