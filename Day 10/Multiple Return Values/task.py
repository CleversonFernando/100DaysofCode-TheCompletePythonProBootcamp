def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you need to type something"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("Type your first name"), input("Type your last name")))

