#Handles data saving and stuff
from stockObj import *

#saves a stock to file, as well as -$ the money
def saveToFile(objs, cash):
    writeData = open('data.txt', 'w')
    writeData.write(cash + '\n')
    for obj in objs:
        data = str(obj.price) + '-&-' + str(obj.shares) + '-&-'
        data += str(obj.ticker) + '-&-' + str(obj.gid)
        writeData.write(data + '\n')
    writeData.close()

#This is how the data is parsed at app launch
def readDataFromFile():
    f = open('data.txt', 'r')
    content = f.readlines()
    content = [line.strip('\n') for line in content]
    cash = content.pop(0)
    objects = []
    #parse to objects
    for val in content:
        data = val.split('-&-')
        objects.append(Equity(data[0], data[1], data[2], data[3]))
    f.close()
    return [cash, objects]