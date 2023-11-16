import requests

def getStocks():
    
    url = "https://bb-finance.p.rapidapi.com/market/get-full"

    querystring = {"id": "ANA:SM,ANE:SM,AENA:SM,ACX:SM,AMS:SM,ACS:SM,SAN:SM,BBVA:SM,CABK:SM,CLNX:SM,ENG:SM,ELE:SM,FER:SM,GRF:SM,IAG:SM,IBE:SM,ITX:SM,IDR:SM,MAP:SM,MEL:SM,NTGY:SM,REP:SM,TEF:SM,UNI:SM,SLR:SM,SOL:SM"}

    headers = {
        "X-RapidAPI-Key": "5ef4ff6610msh94da71473b98d63p14ac16jsn994619dd7994",
        "X-RapidAPI-Host": "bb-finance.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    stocks = {}
    for result_id, result in data["result"].items():
        stocks[result_id] = {
            "name": result["name"],
            "lastPrice": result["last"]
        }
    #print(stocks[result_id])
    #print(stocks)
    return stocks