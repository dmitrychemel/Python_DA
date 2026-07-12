class AgeError(Exception):
   def __init__(self, value):
       super().__init__(value)
       self.value = value

   def __str__(self):
       return repr(self.value)

clients = [
    {'name': 'Alice', 'age': 'ten', 'country': 'USA'},
    {'name': 'Bob', 'age': 35, 'country': 'Canada'},
    {'name': 'Carol', 'age': 40, 'country': 'USA'},
]

def check_valid_age(clients):

    for client in clients:
        if not isinstance(client['age'], int):
            raise AgeError(f'{client["name"]} is not an integer')


try:
    check_valid_age(clients)
    print("All valid age checks passed")
except AgeError as err:
    print(err)