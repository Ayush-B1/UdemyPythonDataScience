print("Life Calculator")

name1 = input("Enter you name: ")
name2 = input("Enter another name: ")

name = name1.lower() + name2.lower()

#True counter
Truecounter = name.count("t") + name.count("r") + name.count("u") + name.count("e")
Lovecounter = name.count("l") + name.count("o") + name.count("v") + name.count("e")

Truecounter = str(Truecounter)
Lovecounter = str(Lovecounter)

Score = Truecounter+Lovecounter

print(f"Your score is {Score}")