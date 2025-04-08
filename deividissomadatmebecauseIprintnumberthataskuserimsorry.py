
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
            want = input("want to make cards? ")
            if want == "yes":
                y = input("quesiton: ")
                g = input("answer: ")
                print("---------------------------------------")
                p[y] = g
            else:
                print("no more cards")
                print("---------------------------------------")
                break
        with open("FlashCards.json", "w") as file:
            json.dump(p, file, indent = 4)



class Student:

    def answer_question():
        r = []
        s = 0
        with open("FlashCards.json", "r") as file:
            d = json.load(file)

        for card, c in d.items():
            print(f"quesiton: {card}")
            k = input("what the answer: ")

            if k == c:
                s += 1
                print(f"correct, streaK: {s}")
                print("---------------------------------------")

            else:

                print(f"wrong, streak = {s}, now resetted to 0")
                print("---------------------------------------")
                s = 0 
                
t = input("teacher or student?")

if t == "teacher":
    Teacher.make_cards()

elif t == "student":
    Student.answer_question()









