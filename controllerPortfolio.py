from portfolio import Portfolio
from stock import Stock
import stockApi as api

class ControllerPortfolio():
    def __init__(self):
        self.__portfolios = {}

    # COUNT total of airports in our list
    def countPortfolios(self):
        return len(self.__portfolios)
    
    def validAccountNumber(self, iban):
        if len(iban) != 24:
            return False
        if iban[:2] != 'ES':
            return False

        return True
        """
        ES9100755769278146778871
        """
        
    
    def add_portfolio(self, dni, name, surname, accountNumber, balance):

        if balance < 0:
            raise ValueError
        else:
            if dni not in self.__portfolios:
                newPortfolio = Portfolio(dni, name, surname, accountNumber, balance)
                self.__portfolios[dni] = newPortfolio
        return True

    def delete_portfolio(self, dni):
        if dni in self.__portfolios:
            del self.__portfolios[dni]
            return True
        else:
            return False
        

    def getPortfolioByDni(self, dni):
        if dni in self.__portfolios:
            return self.__portfolios[dni]
    
    def getAllStoks(self):
        myStocks = api.getStocks()
        return myStocks
    
    def buy_stock(self, dni, stock, quantity):
        portfolio = self.__portfolios[dni]

        stocks = self.getAllStoks()

        if stock not in stocks.keys():
            return False
        cash = stocks[stock]["lastPrice"]
        portfolio.buyStock(stock, quantity, float(cash))
        return portfolio
        

    def sell_stock(self, dni, stock, quantity):
        portfolio = self.__portfolios[dni]

        stocks = self.getAllStoks()
        
        if stock not in stocks.keys():
            return False
        
        cash = stocks[stock]["lastPrice"]
        portfolio.sellStock(stock, quantity, float(cash))
        return portfolio

    def list_client_portfolio(self, dni):
        portfolio = self.__portfolios[dni]
        return portfolio
