import log


def wrong_input():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Incorrect entry! Please, choose something from the list!")


def is_number(text):
    while True:
        try:
            number = float(input(text))
            log.log_data(number)
            return number
        except ValueError:
            print("Error! You entered not a number! Try again.")


def is_not_zero(text):
    while True:
        try:
            number = float(input(text))
            if number == 0:
                print("Error! Division by 0! Enter another number.")
            else:
                log.log_data(number)
                return number
        except ValueError:
            print("Error! You entered not a number! Try again.")
