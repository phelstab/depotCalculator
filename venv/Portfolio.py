import math
import yfinance as yf
import json

class Portfolio:
    ## Yahoo Finance Short Name z.B. XWD.To für den MSCI World Index
    stock1 = "XWD.To"
    stock2 = "EEM"
    stock3 = "IBCQ.F"

    ## Prozentanteil der Verteilung der Aktien
    share1 = 0.45
    share2 = 0.15
    share3 = 0.40

    ## Anlage Guthaben
    pay = 1000



def calcIndex(stockName):
    stockInfo = yf.Ticker(stockName)
    # some JSON:
    x = stockInfo.info

    # parse x:
    s1 = json.dumps(x)
    d2 = json.loads(s1)

    # the result is a Python dictionary:
    return (d2['previousClose'])

def getName(stockName):
    stockInfo = yf.Ticker(stockName)
    # some JSON:
    x = stockInfo.info

    # parse x:
    s1 = json.dumps(x)
    d2 = json.loads(s1)

    # the result is a Python dictionary:
    return (d2['longName'])

stockPrice1 = calcIndex(Portfolio.stock1)
stockPrice2 = calcIndex(Portfolio.stock2)
stockPrice3 = calcIndex(Portfolio.stock3)
stockName1 = getName(Portfolio.stock1)
stockName2 = getName(Portfolio.stock2)
stockName3 = getName(Portfolio.stock3)
print(stockName1 , ': ' , stockPrice1 , ' €')
print(stockName2 , ': ' , stockPrice2 , ' €')
print(stockName3 , ': ' , stockPrice3 , ' €')


def portfolioCalcu():

    rest1 = (Portfolio.pay * Portfolio.share1) % (stockPrice1)
    rest2 = (Portfolio.pay * Portfolio.share2) % (stockPrice2)
    rest3 = (Portfolio.pay * Portfolio.share1) % (stockPrice3)

    prop1 = math.floor((Portfolio.pay * Portfolio.share1) / (stockPrice1))
    prop2 = math.floor((Portfolio.pay * Portfolio.share2) / (stockPrice2))
    prop3 = math.floor((Portfolio.pay * Portfolio.share3) / (stockPrice3))

    outgoings = prop1 * stockPrice1 + prop2 * stockPrice2 + prop3 * stockPrice3
    bank = Portfolio.pay - outgoings

    print('____________')
    print('Buy (Amount) of', stockName1 , ': ' , prop1 )
    print('Buy (Amount) of', stockName2 , ': ' , prop2 )
    print('Buy (Amount) of', stockName3 , ': ' , prop3 )
    print('Outgoings: ' , outgoings , ' €')
    print('Left on Bank: ' , bank , ' €')

portfolioCalcu()