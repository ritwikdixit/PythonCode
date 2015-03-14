#the stock object model
class Equity:

    #price, shares, ticker, (g)id
    
    def __init__(self, price, shares, ticker, gid):
        self.price = float(price)
        self.shares = int(shares)
        self.ticker = ticker
        self.gid = gid

    def toList(self):
        netval = self.price * self.shares
        allstock = [self.price, self.shares, self.ticker, netval]
        return allstock

    def getNetValue(self):
        return self.price * self.shares

    def __str__(self):
        exspace = '\t' if len(str(self.price)) >= 7 else ''
        netprice = self.shares * self.price
        print 'Ticker', '\t', 'Price', '\t' + exspace, 'Shares', '\t', 'Net Value'
        print self.ticker, '\t', self.price, '\t', self.shares, '\t', netprice
        return ''
