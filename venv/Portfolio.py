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



def calcStock(stockName):
    stockInfo = yf.Ticker(stockName)
    # get JSON through API:
    x = stockInfo.info

    # parse x:
    s1 = json.dumps(x)
    d2 = json.loads(s1)

    return (d2['previousClose'], d2['longName'])


def calcProp(share,price):

    pay = Portfolio.pay
    prop =  math.floor((pay * share) / (price))

    return prop

def portfolioCalcu():

    price1, name1 = calcStock(Portfolio.stock1)
    price2, name2 = calcStock(Portfolio.stock2)
    price3, name3 = calcStock(Portfolio.stock3)

    prop1 = calcProp(Portfolio.share1, price1)
    prop2 = calcProp(Portfolio.share2, price2)
    prop3 = calcProp(Portfolio.share3, price3)

    outgoings = prop1 * price1 + prop2 * price2 + prop3 * price3
    bank = Portfolio.pay - outgoings

    return (price1, price2, price3, name1, name2, name3, prop1, prop2, prop3, outgoings, bank)

def __printResult__():
    p1, p2, p3, n1, n2, n3, p1, p2, p3, o, b = portfolioCalcu()
    print('________________Current Prices________________')
    print(n1, ': ', p1, ' €')
    print(n2, ': ', p2, ' €')
    print(n3, ': ', p3, ' €')
    print('________________Consulting____________________')
    print('Buy (Amount) of', n1, ': ', p1)
    print('Buy (Amount) of', n2, ': ', p2)
    print('Buy (Amount) of', n3, ': ', p3)
    print('Outgoings: ', o, ' €')
    print('Left on Bank: ', b, ' €')

__printResult__()