class Order:
    def __init__(self, order_id, products, total_amount):
        self.order_id = order_id
        self.products = products
        self.total_amount = total_amount

    def calculate_total_amount(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

order1 = Order("ABC1", [Product("Sách Python cơ bản", 150000, 2), Product("Chuột máy tính", 200000, 1)], 0)
order1.total_amount = order1.calculate_total_amount()

order2 = Order("ABC2", [Product("Laptop Dell Inspiron", 15000000, 1), Product("Bàn phím ", 1000000, 1)], 0)
order2.total_amount = order2.calculate_total_amount()

orders = [order1, order2]

for order in orders:
    print("Order ID:", order.order_id)
    print("Total amount:", order.total_amount)

        