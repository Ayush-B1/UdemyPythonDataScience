# the year is divisible by 4 and 400

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is a leap year")
        else:
            print("The year is not a leap year")
    else:
        print("leap year")
else:
    print("Not a leap year")