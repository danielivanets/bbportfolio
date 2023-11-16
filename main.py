import stockApi as api
from controllerPortfolio import ControllerPortfolio
controller = ControllerPortfolio()

while True:
    print("Currently there are", controller.countPortfolios(), "portfolios registered!")
    print("1.- Add a portfolio")
    print("2.- Delete portfolio")
    print("3.- Buy stock for a client")
    print("4.- Sell stock for a client")
    print("5.- List client portfolio")
    print("6.- Exit")
    
    choice = input("Choose option: ")
    


    if choice == "1":
        dni = input("Input DNI: ")
        name = input("Input Name: ")
        surname = input("Input Surname: ")
        accountNumber = input("Input Account Number: ")
        if not controller.validAccountNumber(accountNumber):
            print("Invalid account number...")
            continue
        balance = float(input("Input initial balance: "))
        if balance < 0:
            print("Invalid balance...")
            continue
        
        if(controller.add_portfolio(dni, name, surname, accountNumber, balance)):
            print(f"Portfolio with DNI {dni} added successfully!!!")
        else:
            print("Error adding portfolio")



    elif choice == "2":
        dni = input("Enter DNI to delete portfolio: ")
        if controller.delete_portfolio(dni) == True:
            print(f"Portfolio with DNI {dni} deleted successfully.")
        else:
            print(f"Portfolio with DNI {dni} not found.")
    
    
    
    elif choice == "3":
        dni = input("Input DNI: ")
        print("List of stocks")
        print("---------------")
        #for key,value in controller.getAllStoks():
        #    print("Stock key: " + key + " -> " + value["name"] + ": " + value["lastPrice"])
        for symbol, details in controller.getAllStoks().items():
            print("Stock key: " + symbol + " -> " + details["name"] + ": " + details["lastPrice"])

        stock = input("Select stock: ")
        quantity = int(input("Input quantity: "))

        if controller.buy_stock(dni,stock,quantity):
            print("Stock bought successfully!")
        else:
            print("Error in buy_stock....")
        
    elif choice == "4":
        dni = input("Input DNI: ")
        print("List of stocks")
        print("---------------")
        for symbol, details in controller.getAllStoks().items():
            print("Stock key: " + symbol + " -> " + details["name"] + ": " + details["lastPrice"])

        stock = input("Select stock: ")
        quantity = int(input("Input quantity: "))

        if controller.sell_stock(dni,stock,quantity):
            print("Stock selt successfully!")
        else:
            print("Error in sell_stock....")
            
        



    elif choice == "5":
        stocks = {}
        dni = input("Input DNI: ")
        portfolio = controller.list_client_portfolio(dni)
        print("DNI: ",portfolio.getDNI())
        print("Name: ",portfolio.getName())
        print("Surname: ", portfolio.getSurname())
        print("Account: ",portfolio.getAccountNumber())
        print("Balance: ",portfolio.getBalance())
        print("Stocks:")
        for key, value in portfolio.getSetOfStock().items():
            stocks_info = f"'{key}': {value}"
            print(stocks_info)
        





    elif choice == "6":
        break



    else:
        print("Invalid option. Please choose a valid option (1-6).")