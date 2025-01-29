def format_name(f_name, l_name):
    return f_name.capitalize() + " " + l_name.capitalize()

f_name = input("Type the first name:")
l_name = input("Type your last name:")
print(format_name(f_name, l_name))
