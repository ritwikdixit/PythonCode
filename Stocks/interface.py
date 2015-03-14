#Equity Stocks Game created by Ritwik Dixit on 11/3/13
#Rewritten/Optimized on 3/13/15

#To anyone reading this after Summer 2014:
#Please do not mind that I had no idea how to handle HTTP requests :P

#Usage: type the name of your stock when buying
#Sample buy stock input: 'GOOGL' (no quotes)
#Sample buy stock input: 'BRK.A' (no quotes)
#To Sell, or get report, there are instructions

from addStockScript import *
from stockObj import *
from file_io import *

#global variables
cash = 0.0
objs = []
startCash = 1000000

#gets the real time value of the stocks, updates your holdings
def updateStocks():
    print 'Getting Real Time Data, Please Wait...'
    global objs
    #get new val for all stocks
    for i in range(len(objs)):
        stock = objs[i]
        newStock = Equity(getStockReport(stock)[1], stock.shares, stock.ticker, stock.gid)
        objs[i] = newStock

def reset():
    global cash
    global objs
    reset = open('data.txt', 'w')
    reset.write(str(startCash) + '\n')
    reset.close()
    cash = float(startCash)
    objs = []

#Enter ticker, shares
#Gets the stock from google finance, adds to holdings
def buyStock():
    global cash
    global objs    
    trade_ticker = raw_input('Enter the ticker, i.e. \'GOOGL\': ')
    tshares = raw_input('how many shares would you like to order: ')

    data = []
    try:
        data = getStockData(trade_ticker)
    except:
        print 'Error in finding Stock'
        return 0

    stockid = data[0]
    tprice = data[1]

    stock1 = Equity(tprice, tshares, trade_ticker, stockid)
    if stock1.getNetValue() <= cash:
        objs.append(stock1)
        cash -= stock1.getNetValue()
        saveToFile(objs, str(cash))
        print '\nTRANSACTION COMPLETED\n' + str(stock1)
    else:
        print 'You don\'t have enough money!'

#allows you to 'pop' some of your stocks and sell them for cash
def sellStocks():
    global cash
    global objs
    updateStocks()
    if len(objs) < 1:
        print 'No Stocks to Sell'
        return 0
    global cash
    print 'Enter the index for the stock you would like to sell:'
    for i in range(len(objs)):
        print '[' + str(i) + '] '
        print str(objs[i]) + '\n'
    choice = int(raw_input('>> '))
    try:
        stockToSell = objs.pop(choice)
        cash += stockToSell.getNetValue()
        saveToFile(objs, str(cash))
        print '\nTRANSACTION COMPLETED\n'
    except:
        print 'Stock Sell Error'

#Prints out a Portfolio Holdings Report
def getFullReport():
    updateStocks()    
    print 'Cash = $' + str(cash) + '\n'
    total = 0
    for stoc in objs:
        total += stoc.getNetValue()
        print str(stoc) + getStockReport(stoc)[0] + '\n'
    total += cash
    print 'Your total net worth = $' + str(total)

saved = readDataFromFile()
cash = float(saved[0])
objs = saved[1]
updateStocks()

#The Console Application Menu
print '\n-------Equity Stocks Game Menu-------'
print '>1 to buy stocks \n>2 to sell stocks \n>3 for report\n>4 to quit\n>0 to reset game'
choice = raw_input('>>')
while choice != '4':
    if choice == '0':
        c = raw_input('are you sure you want to reset? Y for Yes >>')
        if c == 'y' or c == 'Y':
            reset()
            print 'Game reset.'
        else: 
            print 'Game not reset.'
    elif choice == '1':
        buyStock()
    elif choice == '2':
        sellStocks()
    elif choice == '3':
        getFullReport()

    print '\n-------Equity Stocks Game Menu-------'
    print '>1 to buy stocks \n>2 to sell stocks \n>3 for report\n>4 to quit\n>0 to reset game'
    choice = raw_input('>>')

