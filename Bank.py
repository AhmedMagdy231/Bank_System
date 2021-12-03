from User import User
from History import  History

class Bank(User):

    def __init__(self, name, age, gender, ID, password,money=0,history=[0,2,3]):
        super().__init__(name, age, gender, ID, password)
        self.__balance = int(money)
        self.History = history

    def getBalance(self):
        return self.__balance
    def setBalance(self,money):
        self.__balance = money



    def deposite(self, money):
        self.__balance += money

    def withDraw(self, money):
        self.__balance -= money


