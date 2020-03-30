import requests

class User:
    baseId = 1
    def __init__(self,userName,loginEmail,passwordHash,updateEmail,updateFrequency,updateConfidence):
        self.__Id = self.baseId
        User.baseId+=1
        self.__userName = userName
        self.__loginEmail = loginEmail
        self.__passwordHash = passwordHash
        self.__updateEmail = updateEmail
        self.__updateFrequency = updateFrequency
        self.__updateConfidence = updateConfidence
        self.__watchList = [] # array of stocks
    
    def getUserName(self):
        return self.__userName
    
    def getId(self):
        return self.__Id

    def getLoginEmail(self):
        return self.__loginEmail
        
    def getUpdateEmail(self):
        return self.__updateEmail
        
    def getUpdateFrequency(self):
        return self.__updateFrequency
    
    def getUpdateConfidence(self):
        return self.__updateConfidence

    def getWatchList(self):
        return self.__watchList # array of stocks

    def setUserName(self,newUser):
        # check db for existence of newUser
        # return success 
        self.__userName = newUser
        return True

    def setLoginEmail(self,newLoginEmail):
        # check db for existence of newLoginEmail
        # return success 
        self.__loginEmail = newLoginEmail
        return True
        
    def setUpdateEmail(self,newUpdateEmail):
        self.__updateEmail = newUpdateEmail
        return True

    def setUpdateFrequency(self, newUpdateFrequency):
        self.__updateFrequency = newUpdateFrequency
        return True
    
    def setUpdateConfidence(self, newUpdateConfidence):
        self.__updateConfidence = newUpdateConfidence
        return True

    def changePassword(self, inputPasswordHash,reInputPasswordHash):
        if inputPasswordHash == reInputPasswordHash and inputPasswordHash == self.__passwordHash:
            self.__passwordHash = inputPasswordHash
            return True
        else:
            return False
    
    def verifyPassword(self, inputPasswordHash):
        if inputPasswordHash == self.__passwordHash:
            return True
        else:
            return False
    
    def addStockToWatchList(self,stock):
        self.__watchList.append(stock)
        return True
    
    def removeStockFromWatchList(self,stock):
        if isinstance(stock,int):
            try:
                self.__watchList.pop(stock)
                return True
            except:
                return False
        else:
            try:
                self.__watchList.remove(stock)
                return True
            except:
                return False
    
    def postUser(self):
        url = "https://us-central1-cz2006-9cd2d.cloudfunctions.net/app/addUser"

        watchListTemp = []

        for stock in self.__watchList:
            watchListTemp.append(str(stock))

        payload = "{\r\n\t\"userName\":\""+self.__userName+"\",\r\n\t\"passwordHash\":\""+self.__passwordHash+"\",\r\n\t\"loginEmail\": \""+self.__loginEmail+"\",\r\n\t\"updateEmail\": \""+self.__updateEmail+"\",\r\n\t\"updateFrequency\": \""+str(self.__updateFrequency)+"\",\r\n\t\"updateConfidence\": \""+str(self.__updateConfidence)+"\",\r\n\t\"watchList\": "+str(watchListTemp)+"\r\n}"
        headers = {
        'Content-Type': 'application/json',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
