
from _typeshed import Self


class Count:

    def __init__(self, number, name, money=0, limit=1000):

        self.__number = number
        self.__name = name   
        self.__money = money
        self.__limit = limit
        print("Your special number is {}".format(self))

    def deposit(self, value):
        self.__money += value

    def withdraw(self, value):
        if(self.__withdraw_check(value)):
            self.__money -= value
        else:
            print("You don't have money and limit for withdraw")
        
    def extract(self):
        print("{}, your money is {}".format(self.name, self.money))

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)
    
    @property
    def money(self):
        return self.__money
    
    @property
    def name(self):
        return self.__name 

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        print("Your limit was {}".format(self.__limit))
        self.__limit = limit  
        print("Your new limit is {}".format(self.__limit)) 

    def __withdraw_check(self, value):
        return (value >= (self.__money + self.__limit))

    @staticmethod
    def my_code_bank():
        return "001"

    @staticmethod
    def all_code_banks():
        return {"BB":"001", "Box":"104", "Bradesco":"237"}


            
        