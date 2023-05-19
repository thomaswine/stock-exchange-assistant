from stock_api import StockApi

stockApi = StockApi()

class AssistantMenu:
    
    stock_symbol = input("Type company stock exchange symbol: ").upper()
    company_info = stockApi.getCompanyCashflowData(stock_symbol)
    
    