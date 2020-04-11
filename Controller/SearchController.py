import requests
from bs4 import BeautifulSoup

class SearchController:
    @staticmethod
    def search(stockName, t, numOfArticles):

        timePara = ""
        if t == 'Last Hour':
            timePara = " when:1h"
        elif t == 'Last Day':
            timePara = " when:1d"
        elif t == 'Last Week':
            timePara = " when:7d"
        elif t == 'Last Year':
            timePara = " when:1y"

        query = "https://news.google.com/rss/search?q=" + stockName + timePara
        code = requests.get(query)
        soup = BeautifulSoup(code.text,'html5lib') 
        count = 0
        newsDict = {}
        average = 0

        for item in soup.find_all('item'):
            title = (item.title.contents[0])

            date = (item.pubdate.contents[0])
            link = (item.contents[2])
            newsDict[title] = {"Date": date, "Link": link}
            
            count += 1
            if count == numOfArticles:
                break
        return newsDict

if __name__ == "__main__":
    print(SearchController().search("Apple",'Last Hour',5))