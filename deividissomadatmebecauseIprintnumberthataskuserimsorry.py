
""" class Calculator():
    def add(x,y):
        print(x + y)
        return x + y
    def add_many(list):
        print(sum(list))
        return sum(list)
    def subtract(list):
        return list
Calculator.add() """

class Merchant:
    def _init_(self, name, products):
        self.name = name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(self.products)
Joanna = Merchant("Joanna", ['Chicken', 'prok', 'beef'])
Joanna.sell('prok')






