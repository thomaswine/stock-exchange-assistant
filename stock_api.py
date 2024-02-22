import requests
import datetime as dt
from datetime import timedelta, datetime
import json
from graph_module import GraphModule

class StockApi:
    
    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    STOCK_API_KEY = "API_KEY"
    
    def getCompanyLastDayPrices(self):
        
        self.stock_symbol = input("Type stock symbol: ")
        
        company_prices = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": self.stock_symbol,
            "apikey": self.STOCK_API_KEY
        }
        
        today = dt.datetime.now().date()
        yesterday = str(today - timedelta(days=1))
        
        response = requests.get(self.STOCK_ENDPOINT, params=company_prices)
        yesterday_closing_price = float(response.json()["Time Series (Daily)"][yesterday]["4. close"])
        
        return(yesterday_closing_price)
    
    
    def searchForCompany(self):
        
        self.company_name = input("Type company name: ")
        
        company_search = {
            "function": "SYMBOL_SEARCH",
            "keywords": self.company_name,
            "apikey": self.STOCK_API_KEY
        }
        
        response = requests.get(self.STOCK_ENDPOINT, params=company_search)
        company_symbol = response.json()["bestMatches"][0]["1. symbol"]
        
        return(company_symbol)
    
    
    def getCompanyCashflowData(self, stock_symbol):
        
        graph_creator = GraphModule()
        
        netIncomes = []
        quarters = []
        
        company_informations = {
            "function": "CASH_FLOW",
            "symbol": stock_symbol,
            "apikey": self.STOCK_API_KEY
        }
        
        response = requests.get(self.STOCK_ENDPOINT, params=company_informations)
        company_info = response.json()["quarterlyReports"]
        #pretty = json.dumps(company_info, indent=4)
        
        
        for quarter in range(len(company_info)):
            netIncome = int(company_info[quarter]["netIncome"])
            quarterDate = str(company_info[quarter]["fiscalDateEnding"])
            
            date_object = datetime.strptime(quarterDate, '%Y-%m-%d').date()
            new_date = f"{date_object.year}-{date_object.month}"
            
            netIncomes.append(netIncome)
            quarters.append(new_date)
            
        reversedNetIncomes = list(reversed(netIncomes))
        reversedQuarters = list(reversed(quarters))
        
        graph = graph_creator.createGraph(reversedQuarters, reversedNetIncomes, stock_symbol, "Quarters", "Net Incomes")
        
        return(graph)
