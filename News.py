class News:
    def __init__(self,description,confidenLevel):
        self.__description = description
        self.__confidenLevel = confidenLevel

    def getDescription(self):
        return self.__description

    def getConfidenLevel(self):
        return self.__confidenLevel
