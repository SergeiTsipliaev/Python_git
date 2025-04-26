from idlelib.iomenu import encoding

from tabulate import tabulate
import json


humans = "humans.json"


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print(f"My name {self.name}")

    def __str__(self):
        return f"{self.name} my name!"


class Worker(Human):

    def __init__(self, name, age, work="Work"):
        super().__init__(name, age)
        self.work = work

    def greetings(self):
        print(f"My name {self.name}. An i work in {self.work} ")


worker1 = Worker("ivan", 39, "ruh")


print(worker1.greetings())
