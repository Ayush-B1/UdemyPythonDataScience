def prime_calc(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("This is a prime number")
    else:
        print("This is not a prime number")


n = int(input("Enter the number to check: "))
prime_calc(n)