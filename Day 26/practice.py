# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
#
# print(new_list)
import random

# name = "Cleverson"
# new_list = [letter for letter in name]
#
# print(new_list)


# new_range = [n+n for n in range(1,5)]
#
# print(new_range)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# # new_name_list = [name for name in names if len(name) <= 4]
# new_name_list = [name.upper() for name in names if len(name) >=5]
#
# print(new_name_list)


names = ["Alex", "Beth", "Caroline"]

student_score = {student: random.randint(1, 100) for student in names}
passed = {student: score for (student, score) in student_score.items() if score > 60}
