# using for loops using range function
target = int(input("Enter a number: "))
target += 1
sum = 0
for even_number in range(2, target, 2):
    sum += even_number

print(sum)
