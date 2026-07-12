class NumberError(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __str__(self):
        return repr(self.value)

def check_number(number):
    if number == "":
        return False
    if number[0] == "-":
        if len(number) == 1:
            return False
        return number[1:].isdigit()

    return number.isdigit()


number = input("Enter product price: ")

try:
    if not check_number(number):
        raise NumberError("The input contains letters or invalid characters.")

    if int(number) < 0:
        raise NumberError("The input contains negative numbers.")

    print(f"Correct price: {number}")

except NumberError as err:
    print(err)






