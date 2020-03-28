import streamlit as st
import requests
from bs4 import BeautifulSoup

class SearchDisplay:

    lastHourPara = " when:1h"
    lastDayPara = " when:1d"
    lastWeekPara = " when:7d"
    lastYearPara = " when:1y"

    @staticmethod
    def search(stockName, t, numOfArticles):
        # if stockName:
        #     results = {
        #         "stockName":"APPLE",
        #         "confidenceLevel":100,
        #         "description":"Just another article"
        #     }
        #     return results

        if stockName == "":
            return ""

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

        for item in soup.find_all('item'):
            title = (item.title.contents[0])
            date = (item.pubdate.contents[0])
            link = (item.contents[2])
            newsDict[title] = [date, link]
            
            count += 1
            if count == numOfArticles:
                break

        return newsDict





    @staticmethod
    def displayResults(results):
        st.write(results)
        # if results:
        #     st.markdown('# '+results["stockName"])
        #     st.write('## '+results["description"],results["confidenceLevel"])

    def renderDisplay(self):
        st.markdown('# HOME')
        timeRange = st.selectbox("Select Time Range",('Last Hour', 'Last Day', 'Last Week', 'Last Year'))
        numOfArticles = st.slider("Select number of articles")
        stockName = st.text_input("Please enter the stock name here")
        searchResults = self.search(stockName,timeRange,numOfArticles)
        self.displayResults(searchResults)


if __name__ == "__main__":
    SearchDisplay().renderDisplay()