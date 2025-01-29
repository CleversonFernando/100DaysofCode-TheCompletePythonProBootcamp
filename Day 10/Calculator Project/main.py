import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)
    first_number = float(input("What is the first number?:\n"))

    confirmation = 'y'

    while confirmation == 'y':
        operation = str(input("+\n-\n*\n/\nPick an operation:"))
        second_number = float(input("What is the next number?\n"))

        if second_number == 0 and operation == "/":
            print("Can't be divide by zero!")
            confirmation = "n"
        else:
            result = operations[operation](first_number, second_number)
            print(f"{first_number} {operation} {second_number} = {result}")
            confirmation = input(f"Type 'y' to continue calculating with {result}")
            first_number = result

    print("finishing calculation!")
    print("\n" * 20)
    calculator()


calculator()
