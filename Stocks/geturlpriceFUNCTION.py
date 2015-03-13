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

import urllib

stock = raw_input('enter the google finance cid no spaces: ')
def get_stock_price(urlgoog):
    source = urllib.urlopen(urlgoog)
    info = source.read()
    #finding the tag displaying the value
    htmlIdTag = 'ref_' + urlgoog[urlgoog.find('=') + 1:] + '_l\">'
    startIndex = info.find(htmlIdTag) + len(htmlIdTag)
    stock_price = info[startIndex : info.find('<',startIndex) - 1]
    return stock_price

def get_ticker(daturl):
    extract = urllib.urlopen(daturl)
    source = extract.read()
    tag = source.find('<title>') + len('<title>')
    start = source.find(':', tag) + 2
    return source[start:source.find('quotes',start) - 1]

#debugging
#print get_ticker('https://www.google.com/finance?cid=' + stock)
#print get_stock_price('https://www.google.com/finance?cid=' + stock)
            
                            
                            
                            
