class DateError(Exception):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    def __str__(self):
        return repr(self.value)

def check_date(value):
    parts = value.split('-')

    if len(parts) != 3:
        raise DateError("Invalid date format")

    day, month, year = parts

    if len(day) !=2 or len(month) !=2 or len(year) !=4:
        raise DateError("Invalid date format")

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        raise DateError("Invalid date format")

    print("Date format is correct")

date = input("Enter date (dd-mm-yyyy): ")

try:
    check_date(date)
except DateError as err:
    print(err)