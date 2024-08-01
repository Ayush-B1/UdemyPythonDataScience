list1 = [" ", " ", " "]
list2 = [" ", " ", " "]
list3 = [" ", " ", " "]
map = [list1, list2, list3]
print(map)
print("Hiding your treasure X marks the spot")

A = [list1[0], list2[0], list3[0]]

position = input("Enter your pos: ")

letter = position[0].lower()  # First letter is lower

abc = ["a", "b", "c"]  # yeh kyu banaya nhi pata # edit future me abb pata hai kyu banaya

letter_index = abc.index(letter)
# print(letter_index)
number_index = int(position[1]) - 1
# print(number_index)
map[number_index][letter_index] = "X"

print(f"{list1}\n{list2}\n{list3}")