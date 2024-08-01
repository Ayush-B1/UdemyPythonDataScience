print("Thank you for choosing python pizza orders")
size = input("type 'L' for large pizza 'M' for medium and 's' for small: ")
L_pizza = 25
M_pizza = 20
S_pizza = 15

if size == 'L':
    pepperoni = input("do you want to add pepperoni in your pizza 'Y' for yes 'N' for no: ")
    if pepperoni == "Y":
        L_pizza += 3
        cheese = input("do you want to add Cheese in your pizza 'Y' for yes 'N' for no: ")
        if cheese == 'Y':
            L_pizza += 1
            print(f"Thank you for choosing Python Pizza your final bill is ${L_pizza}")
        else:
            print(f"Thank you for choosing Python Pizza your final bill is ${L_pizza}")
    else:
        print(f"Thank you for choosing Python Pizza your final bill is ${L_pizza}")
elif size == 'M':
    pepperoni = input("do you want to add pepperoni in your pizza 'Y' for yes 'N' for no: ")
    if pepperoni == "Y":
        M_pizza += 3
        cheese = input("do you want to add Cheese in your pizza 'Y' for yes 'N' for no: ")
        if cheese == 'Y':
            M_pizza += 1
            print(f"Thank you for choosing Python Pizza your final bill is ${M_pizza}")
        else:
            print(f"Thank you for choosing Python Pizza your final bill is ${M_pizza}")
    else:
        print(f"Thank you for choosing Python Pizza your final bill is ${M_pizza}")
elif size == 'S':
    pepperoni = input("do you want to add pepperoni in your pizza 'Y' for yes 'N' for no: ")
    if pepperoni == "Y":
        S_pizza += 2
        cheese = input("do you want to add Cheese in your pizza 'Y' for yes 'N' for no: ")
        if cheese == 'Y':
            S_pizza += 1
            print(f"Thank you for choosing Python Pizza your final bill is ${S_pizza}")
        else:
            print(f"Thank you for choosing Python Pizza your final bill is ${S_pizza}")
    else:
        print(f"Thank you for choosing Python Pizza your final bill is ${S_pizza}")
else:
    print("Enter a valid option")