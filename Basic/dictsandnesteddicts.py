# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                             "Function": "A piece of code that you can easily call over and over again."
# }
#
# # print(programming_dictionary["Bug"])
# #
# # programming_dictionary["Ayush"] = "A professional dumbass"
# #
# # # print(programming_dictionary["Ayush"])
# #
# # for i in programming_dictionary:
# #     print(i)
# #
# # print(programming_dictionary["Ayush"])
#
# capitals = {"Delhi": ["Rajori Garden", "Vasant kunj", "Karol Bagh", "India Gate"],
#             "Gurugram": ["Trampoline Park", "Sector 4 foodie corner", "MG ROAD", "CyberCity"],
#             "Uttarakhand": ["Dheradun", "Massorie", "Haridwar", "Rishikesh"],
#             "Uttarpardesh": ["Noida", "Gaziabad", "Indrapuram"]
# }
#
# employees = {
#     "01": {"Name": "Spongebob", "Age":20, "IS_Active": True, "Date_joined": "12/07/2024", "City_visited": ["Rajori Garden", "Vasant kunj", "Karol Bagh", "India Gate"]},
#     "02": {"Name": "Patrik", "Age":20, "IS_Active": True, "Date_joined": "12/07/2024", "City_visited": ["Dheradun", "Massorie", "Haridwar", "Rishikesh"]}
# }
#
# employees1 = [
#     {"01": {"Name": "Spongebob", "Age":20, "IS_Active": True, "Date_joined": "12/07/2024", "City_visited": ["Rajori Garden", "Vasant kunj", "Karol Bagh", "India Gate"]}},
#      {"02": {"Name": "Patrik", "Age":20, "IS_Active": True, "Date_joined": "12/07/2024", "City_visited": ["Dheradun", "Massorie", "Haridwar", "Rishikesh"]}}
# ]
#
# print(employees1[0])
#
# for id, row in employees.items():
#     print(id, row["Name"], row["City_visited"])
#

# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }
#
# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }
#
# starting_dictionary["c"] = 7
# final_dictionary = starting_dictionary

# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
#
# for key in dict:
#     dict[key] += 1
#
# print(dict)
# dict["c"] = [1, 2, 3]
# print(dict)
#
# print(dict[1])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}


print(order["main"][2])