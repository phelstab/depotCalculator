import math
import yfinance as yf
import json


class Portfolio():


    ## Konstruktor
    def __init__(self, pstock1, pstock2, pstock3, pshare1, pshare2, pshare3, ppay):
        ## Yahoo Finance Short Name z.B. XWD.To für den MSCI World Index
        ## Toronot stock prices
        self.stock1 = pstock1
        self.stock2 = pstock2
        self.stock3  = pstock3

        ## Prozentanteil der Verteilung der Aktien
        self.share1 = pshare1
        self.share2 = pshare2
        self.share3 = pshare3

        ## Anlage Guthaben
        self.pay = ppay

    def calcStock(self, stockName):
        stockInfo = yf.Ticker(stockName)
        # get JSON through API:
        x = stockInfo.info

        # parse x:
        s1 = json.dumps(x)
        d2 = json.loads(s1)

        return (d2['previousClose'], d2['longName'])

    def calcProp(self, share, price):

        pay = self.pay
        prop =  math.floor((self.pay * share) / (price))

        return prop


    def portfolioCalcu(self):

        (price1, name1) = self.calcStock(self.stock1)
        (price2, name2) = self.calcStock(self.stock2)
        (price3, name3) = self.calcStock(self.stock3)

        prop1 = self.calcProp(self.share1, price1)
        prop2 = self.calcProp(self.share2, price2)
        prop3 = self.calcProp(self.share3, price3)

        outgoings = prop1 * price1 + prop2 * price2 + prop3 * price3
        bank = self.pay - outgoings

        return (price1, price2, price3, name1, name2, name3, prop1, prop2, prop3, outgoings, bank)

    ## Just for Testing Results
    def __printResult__(self):

        (p1, p2, p3, n1, n2, n3, prop1, prop2, prop3, o, b) = self.portfolioCalcu()
        print('________________Current Prices________________')
        print(n1, ': ', p1, ' €')
        print(n2, ': ', p2, ' €')
        print(n3, ': ', p3, ' €')
        print('________________Consulting____________________')
        print('Buy (Amount) of', n1, ': ', prop1)
        print('Buy (Amount) of', n2, ': ', prop2)
        print('Buy (Amount) of', n3, ': ', prop3)
        print('Outgoings: ', o, ' €')
        print('Left on Bank: ', b, ' €')
