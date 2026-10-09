def get_operation():
    while True:
        try:
            operation= int(input("Choose an operation (1-6): "))
            if 1<operation>6:
                return operation
            else:
                print("please enter a number between 1 to 6")
        except ValueError:
            print("Invalid input. Please enter a number")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")

c = get_operation()
a = get_number("Enter the first number: ")
b = get_number("Enter the second number: ")

match c:
    case 1:
        print("The addition of", a, "and", b, "is", a + b)

    case 2:
        print("The subtraction of", a, "and", b, "is", a - b)

    case 3:
        print("The multiplication of", a, "and", b, "is", a * b)

    case 4:
        if b == 0:
            print("Invalid: cannot divide by zero.")
        else:
            print("The division of", a, "and", b, "is", a / b)

    case 5:
        if b == 0:
            print("Invalid: cannot divide by zero.")
        else:
            print("The floor division of", a, "and", b, "is", a // b)

    case 6:
        print("The exponential of", a, "to", b, "is", a ** b)

    case _:
        print("Please enter a valid operation.")