print("Welcome to treasure Island")
print("Your Mission is to find treasure")
Direction = input("Choose your direction 'left' or 'right': ")
Direction = Direction.lower()
if Direction == "left":
    question = input("Swim or wait: ")
    question = question.lower()
    if question == "swim":
        print("Game Over")
    else:
        anotherQuestion = input("Which door? 'RED' or 'BLUE' or 'YELLOW': ")
        anotherQuestion = anotherQuestion.lower()
        if anotherQuestion == "red":
            print("Game Over")
        elif anotherQuestion == 'blue':
            print("Game Over")
        else:
            print("YOU WIN")
else:
    print("GAme Over")


