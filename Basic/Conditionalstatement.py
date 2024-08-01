print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cms: "))
photo = input("Do you want a photo: ")
if height >= 120:
    print("Enjoy the ride")
    age = int(input("Enter your Age: "))
    if age > 17:
        if photo == "yes":
            print("please pay $12+$3 for the ride")
        else:
            print("please pay $12 for the ride")
    elif age < 12:
        if photo == "yes":
            print("Please pay $5+$3 for the ride")
        else:
            print("Please pay $5 for the ride")
    else:
        if photo == "yes":
            print("please pay $7+$3 for the ride")
        else:
            print("please pay $7 for the ride")
else:
    print("You cant ride the roller coaster")