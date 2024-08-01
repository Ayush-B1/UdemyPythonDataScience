# 1 can of paint can cover 5 square meter
import math


def paintcanarea(height, width):
    numbers_of_cans = (height*width) / 5
    print(f"You need {math.ceil(numbers_of_cans)} to paint the wall")


height = int(input("Enter Height"))
width = int(input("Enter width"))

paintcanarea(height, width)

