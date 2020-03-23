class Stock:
    def __init__(self,stockName,userID,confidenSet,stockPrice,stockInfo):
        self.__stockName = stockName
        self.__userID = userID
        self.__confidenSet = confidenSet
        self.__stockPrice = stockPrice
        self.__stockInfo = stockInfo
        self.__newsList = []  # array of news

    def getStockName(self):
        return self.__stockName

    def getUserID(self):
        return self.__userID

    def getConfidenSet(self):
        return self.__confidenSet

    def getStockPrice(self):
        return self.__stockPrice

    def getStockInfo(self):
        return self.__stockInfo




