#This script will take the stock ticker
#like 'NASDAQ:TSLA' or 'TWTR', return the id, and price
#Handles internet connections with urllib

import urllib

#Inefficient but meh
def get_price_from_source_id(info, gid):
    htmlIdTag = 'ref_' + gid + '_l\">'
    startIndex = info.find(htmlIdTag) + len(htmlIdTag)
    stock_price = info[startIndex : info.find('<',startIndex)].replace(',', '')
    return stock_price

#usage: tick should be market:stock ticker, i.e.
#tick = 'NYSE:GE'
#tick = 'NASDAQ:TSLA'
#returns ID & stock price
def getStockData(tick):
    url = 'https://www.google.com/finance?q=' + tick
    source = urllib.urlopen(url)
    info = source.read()
    #find the cid
    tag = '<link rel=\"canonical\" href=\"'
    
    startSearchIndex = info.find(tag) + len(tag)
    gidIndex = info.find('=', startSearchIndex) + 1
    gid = info[gidIndex:info.find('\">', gidIndex)]

    #id found, get stock price
    return [gid, get_price_from_source_id(info, gid)]

#gets old stock objects id to see change
def getStockReport(stock):
    info = urllib.urlopen('https://www.google.com/finance?cid=' + stock.gid).read()
    newprice = float(get_price_from_source_id(info, stock.gid))
    change = newprice - stock.price
    return ('This stock has changed by: $' + str(change), newprice)
