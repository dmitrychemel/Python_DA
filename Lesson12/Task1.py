class Product:
    def __init__(self, name, price, description, ):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Name: {self.name} \nPrice: {self.price} \nDescription: {self.description} \n"

class Customer:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name} \nSurname: {self.surname} \nPhone: {self.phone} \nE-mail: {self.email}"


class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    def sum_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.price
        return total_price

    def __str__(self):
        products = "\n".join([str(product) for product in self.products])
        return (f" ==== ORDER ===== \n"
                f"CUSTOMER:\n Name: {self.customer.name} \n Surname: {self.customer.surname} \n"
                f"Products:\n {products}"
                f"Total price: {self.sum_price()}")

product1 = Product("Milk", 20, "Other")
product2 = Product("Apple", 10, "Fruit")
product3 = Product("Banana", 20, "Fruit")

customer1 = Customer("Billy", "Waserman", "+234283249", "Billy@gmail.com")
order1 = Order(customer1, products =[product1, product2, product3])
print(order1)
