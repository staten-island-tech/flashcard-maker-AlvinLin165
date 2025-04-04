
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
        p = {}
        while True:
            want = input("want make cards? ")
            if want == "yes":
                y = input("quesiton: ")
                g = input("answer: ")
                p[y] = g
            else:
                print("no more")
                break
        with open("FlashCards.json", "w") as file:
            json.dump(p, file, indent = 4)

Teacher.make_cards()

class Student:

    def answer_question():
        r = []
        s = 0
        with open("FlashCards.json", "r") as file:
            d = json.load(file)

        for card in d:
            print(card)
            k = input("what the answer: ")

            if k == card:
                print("correct")
                s += 1
                print(f"streaK: {s}")

            else:
                print("wrong")
                print(f"streak = {s}, now rested to 0")
                s = 0 
                
Student.answer_question()









