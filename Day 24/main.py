# with open("my_file.txt") as file:
#     content = file.read()
#
#     print(content)
from os import write

with open("new_my_file.txt", mode="w") as file:
    file.write("\nhello 3")

