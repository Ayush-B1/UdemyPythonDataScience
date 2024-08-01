import math

student_height = input("Enter your height: ").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

sum = 0
for i in student_height:
    sum = sum + i

print(f"Total height = {sum}")

avg = sum/len(student_height)
print(int(math.ceil(avg)))