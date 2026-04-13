year = int(input("enter year: "))

if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year")
    else:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Normal year")
else:
    print("Normal year")
    
    
    
    
