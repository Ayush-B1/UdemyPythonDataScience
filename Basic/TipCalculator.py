print("Welcome to tip calculator!!!")

bill = float(input("What was the total bill? $"))
tip_percentage = float(input("Amount you would like to tip 10, 12 or 15? $"))
bill_split = int(input("How Many People to Split the bill? "))
percentage = tip_percentage/100
# print(percentage)
total_bill = (bill*percentage) + bill
pay = total_bill/bill_split


print(f"each person should pay ${"{:.2f}".format(round(pay, 2))}")
