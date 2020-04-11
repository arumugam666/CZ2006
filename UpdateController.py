from Model.User import User
import time
import requests
import json
from Controller.SearchController import SearchController
from Controller.PredictionController import PredictionController
from MailController import main,sendEmail
class UpdateController:
    pass

if __name__ == "__main__":
    service = main()
    # while True:
    
    url = "https://us-central1-cz2006-9cd2d.cloudfunctions.net/app"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    users = response.json()

    watchlistDict = {}
    allEmails = set()
    for value in users.values():
        for stock in value["watchList"]:
            if stock in watchlistDict.keys():
                watchlistDict[stock].append((value["updateEmail"],int(value["updateConfidence"])))
                allEmails.add(value["updateEmail"])
            else:
                watchlistDict[stock] = [(value["updateEmail"],int(value["updateConfidence"]))]
                allEmails.add(value["updateEmail"])

    allEmails = list(allEmails)
    emailDict = {email:[] for email in allEmails}
    selfMessage = []
    for stock,emailConfTup in watchlistDict.items():
        # print("Assessing Stock {}\n".format(stock))
        searchResults = SearchController.search(stock,"Last Hour",5)
        predictionResults = PredictionController.predict(searchResults)
        for title,value in predictionResults[0].items():
            # print("Title: {}\nLink: {}\nPrediction Value:{}\n".format(title,value["Link"],value["Prediction Value"]))
        
            for email,conf in emailConfTup:
                if value["Prediction Value"]>conf/100 or value["Prediction Value"]<(100-conf)/100:
                    emailDict[email].append("Title: {}\nLink: {}\nPrediction Value: {}\n".format(title,value["Link"],value["Prediction Value"]))
                    # print("         Sending Email to {}\n\n".format(email))
                else:
                    selfMessage.append("Not sending email to {}\nTitle: {}\nPrediction Value: {}\n".format(email,title,value["Prediction Value"]))

                    # print("         Not Sending Email to {}\n\n".format(email))
    
    for email, contentList in emailDict.items():
        if contentList:
            print("Content List: ",contentList)

            sendEmail(service,email,"Stock Updates","Greetings!\n\nWe've prepared the following set of stock Updates for you!\n\n"+"\n".join(contentList))

    sendEmail(service,'teamalphacz2006@gmail.com',"Update","\n".join(selfMessage))

    # print(watchlistDict)
    # time.sleep(300)
        
