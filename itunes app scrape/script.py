#Ritwik Dixit 2015
#scrape data of the top 100 free apps on the itunes store
#**As of March 2015, 3 of the apps are fake

import urllib

url = 'https://www.apple.com/itunes/charts/free-apps/'
page = urllib.urlopen(url).read()

#given string, search, finish find the part within end or search and end
#i.e. utilfind('I am an example argument.', 'am an ', ' argument') returns 'example'
def utilfind(searchstr, query, endquery):
    return searchstr[searchstr.find(query) + len(query):searchstr.find(endquery, searchstr.find(query))]

#find the area where the top 100 apps are, then start searching
startcut = page.find('<section class="section apps chart-grid">')
end = page.find('/ul', startcut)
shortpage = page[startcut:end]

#loop through every 'li' and find its href
index = shortpage.find('<li>')
links = []
while index != -1:
    link = shortpage[shortpage.find('href="', index) + len('href="'):shortpage.find('?', index)]
    #these are fake apps, skip their ids
    if link.find('586213247') == -1 and link.find('583845719') == -1 and link.find('940985623') == -1:
        links.append(link)
    index = shortpage.find('<li>', index + 1)

allapps = []
for index, appurl in enumerate(links):
    print 'Getting data for app #' + str(index + 1)
    appsrc = urllib.urlopen(appurl).read()
    shortdata = utilfind(appsrc, 'left-stack', '<div class="app-rating">')
    ratingdata = utilfind(appsrc, '<div>All Versions:</div>', '<span class="rating-star">')

    #find the point in html where the data is and add to dictionary
    appdata = {
        'App Name' : utilfind(appsrc, '<h1 itemprop="name">', '</h1>'),
        'Category' : utilfind(shortdata, 'itemprop="applicationCategory">', '</span>'),
        'Seller' : utilfind(shortdata, 'itemprop="name">', '</span>'),
        'Size' : utilfind(shortdata, 'Size: </span>', '</li>'),
        'Ratings' : utilfind(ratingdata, 'aria-label=\'', '\'><div')
    }
    allapps.append(appdata)

#save to text file
f = open('save.txt', 'w')
for index, dict in enumerate(allapps):
    f.write('Rank: ' + str(index + 1) + '.\n')
    f.write('App Name: ' + dict['App Name'] + '\n')
    f.write('Category: ' + dict['Category'] + '\n')
    f.write('Seller: ' + dict['Seller'] + '\n')
    f.write('Size: ' + dict['Size'] + '\n')
    f.write('Ratings: ' + dict['Ratings'] + '\n\n')

f.close()
