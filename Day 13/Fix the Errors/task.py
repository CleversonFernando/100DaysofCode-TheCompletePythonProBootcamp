def check_age():
    is_a_number = False
    while not is_a_number:
        try:
            age = int(input("How old are you?"))
            is_a_number = True
        except ValueError:
            print("You have typed a invalid number!")
            is_a_number = False

    if age > 18:
        print(f"You can drive at age {age}.")


check_age()
