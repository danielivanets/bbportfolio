import BaseModel
from stock import Stock

class Portfolio(BaseModel.BaseModel):
    def __init__(self,dni,name,surname,accountNumber,balance):
        super().__init__(dni,name,surname)
        self.__accountNumber = accountNumber
        self.__balance = balance
        self.__setOfStock = {}


    def getAccountNumber(self):
        return self.__accountNumber
    def getBalance(self):
        return self.__balance
    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber
    def setBalance(self, balance):
        self.__balance = balance

    
    def getSetOfStock(self):
        return self.__setOfStock
    
    def buyStock(self, stockName, quantity, cash):
        totalCost = quantity * cash
        if self.getBalance() > totalCost:

            if stockName not in self.__setOfStock:
                self.__setOfStock[stockName] = Stock(stockName, quantity)
            else:
                myStock = self.__setOfStock[stockName]
                myStock.setQuantity(myStock.getQuantity() + quantity)
            self.setBalance(self.getBalance() - totalCost)
            return True
        else:
            return False

    def sellStock(self, stockName, quantity, cash):
        #stock = Stock(stockName, quantity)
        if stockName in self.__setOfStock:
            myStock = self.__setOfStock[stockName]
            
            if myStock.getQuantity() >= quantity:
                myStock.setQuantity(myStock.getQuantity() - quantity)

                totalCost = quantity * cash
                if totalCost < self.getBalance(): 
                    self.setBalance(self.getBalance() + totalCost)

                if myStock.getQuantity() == 0:
                    del self.__setOfStock[stockName]

                return True
            return False
            
        

