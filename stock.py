class Stock():
    def __init__(self,name,quantity):
        self.__name = name
        self.__quantity = quantity

    def getName(self):
        return self.__name
    def getQuantity(self):
        return self.__quantity

    
    def setName(self, name):
        self.__name = name
    def setQuantity(self, quantity):
        self.__quantity = quantity

    def __str__(self):
        return f"Name: {self.__name}, Quantity: {self.__quantity}"