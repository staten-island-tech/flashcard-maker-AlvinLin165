
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
        want = input("want make cards? ")

        p = {}

        if want == "yes":
            y = input("quesiton: ")
            g = input("answer: ")
            p[y] = g
        else:
            print("no more")


        while want == "yes":
            want = input("want to make? ")
            if want == "yes":
                y = input("quesiton: ")
                g = input("answer: ")
                p[y] = g
            else:
                print("ok stop")

        with open("FlashCards.json", "w") as file:
                json.dump(p, file, indent = 4)

Teacher.make_cards()


class Student:
    
    def answer_question():
        with open("FlashCards.json") as file:
            d = json.load(file)

        for card in d:
            print(f"question: {card}")
            k = input("what the answer: ")
            if k == d:
                print("correct")
        else:
            print("wrong")
Student.answer_question()









