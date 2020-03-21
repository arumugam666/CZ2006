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

    def getUpdateFrequency(self, newUpdateFrequency):
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
    
    def addStockToWatchList(stock):
        self.__watchList.append(stock)
        return True
    
    def removeStockFromWatchList(stock):
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