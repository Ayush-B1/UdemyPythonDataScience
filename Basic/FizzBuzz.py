# if the number is divisible by 3 print Fizz
# if the number is divisible by 5 print Buzz
# if the number is divisible by both print "FizzBuzz"

number = int(input("Enter a number: "))
for game in range(1, number + 1):
    if game%3 == 0 and game%5 == 0:
        print("FizzBuzz")
    elif game % 3 == 0:
        print("Fizz")
    elif game % 5 == 0:
        print("Buzz")
    else:
        print(game)
