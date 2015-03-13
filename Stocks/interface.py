#url google_finance >>> python EQUITY created by Ritwik Dixit 11/3/13

# Instructions if you are running this
# copy paste the url in GOOGLE FINANCE ONLY of the desired stock

#To anyone reading this after Summer 2014:
#This function was made a long time ago
#Please do not mind that I had no idea how to handle HTTP requests :P
#Please do not mind the funny code style, I was still learning Python
#and Object Oriented Concepts at the time

#Usage: type the name of your stock into google
#Click on the stock, in the url, get the cid value and paste it in here.
#i.e. google search 'GOOG', click stock, cid = 304466804484872

from geturlpriceFUNCTION import *

class Equity:

    #data = price, shares, ticker, (g)id
    
    def __init__(self, price, shares, ticker, gid):
        self.price = float(price)
        self.shares = int(shares)
        self.ticker = ticker
        self.gid = gid

    def back(self):
        netval = self.price * self.shares
        allstock = [self.price, self.shares, self.ticker, netval]
        return allstock

    def __str__(self):
        netprice = self.shares * self.price
        print "Trade & Ticker", "\t", "Price", "\t", "Shares", "\t", "Net Value"
        print self.ticker, "\t", self.price, "\t", self.shares, "\t", netprice
        return ''

def saveToFile(obj):
    writeData = open('data.txt', 'a')
    data = str(obj.price) + '-&-' + str(obj.shares) + '-&-'
    data += str(obj.ticker) + '-&-' + str(obj.gid)
    writeData.write(data + '\n')

#gets old data and sees how much the stock has changed value
def getStockReport(stock):
    url = 'https://www.google.com/finance?cid=' + stock.gid
    newprice = float(get_stock_price(url))
    change = newprice - stock.price
    return ('This stock has changed by: ' + str(change), change)


def readDataFromFile():
    f = open('data.txt', 'r')
    content = f.readlines()
    content = [line.strip('\n') for line in content]
    objects = []
    #parse to objects
    for val in content:
        data = val.split('-&-')
        objects.append(Equity(data[0], data[1], data[2], data[3]))
    return objects

def buyStock():
    stockid = raw_input('enter the google finance cid no spaces: ')
    tshares = raw_input('how many shares would you like to order: ')

    stockurl = 'https://www.google.com/finance?cid=' + stockid
    tprice = get_stock_price(stockurl)
    trade_ticker = get_ticker(stockurl)

    stock1 = Equity(tprice, tshares, trade_ticker, stockid)
    print '\nTRANSACTION COMPLETED\n'
    print stock1
    saveToFile(stock1)
    return stock1


objs = readDataFromFile()
for stoc in objs:
    print stoc
    print getStockReport(stoc)[0]
choice = raw_input('1 to buy more objects, 2 to quit >>')
while choice != '2':
    if choice == '1':
        buyStock()
    choice = raw_input('1 to buy more objects, 2 to quit >>')




    
