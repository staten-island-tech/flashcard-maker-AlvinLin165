
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

""" class Merchant:
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(self.products)

Joanna = Merchant("Joanna", ['Chicken', 'pork', 'beef'])
Joanna.sell('pork') """


import json

class Teacher:
    def make_cards():
        y = input("quesiton: ")
        g = input("answer: ")
        p = {}
        p[y] = g
        with open("FlashCards.json", "w") as file:
            json.dump(p, file, indent = 4)

Teacher.make_cards()

for movie in movies:
    break











