class StockDatabase:
    
    def initDatabase(self):

        database = open("./Database/symbols.txt").read().splitlines()
        return(database)

