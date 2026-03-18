# try:
#     file = open('file.txt')
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
#
# except FileNotFoundError:
#     file = open('file.txt', 'w')
#     file.write('something')
#
# except KeyError as e:
#     print(f" the key {e} doesn't exist")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     raise TypeError("this is an error that I made up")

# height  = int(input("Enter Height : "))
# weight = int(input("Enter Weight : "))
#
# if height > 3:
#     raise ValueError("Height should not be greater than 3")
#
# bmi = weight/height ** 2
# print(bmi)

# Test 1
# fruits = ["Apple", "Pear", "Orange"]
#
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass

    return total_likes


count_likes(facebook_posts)
