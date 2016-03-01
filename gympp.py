#import any thing needed
import requests
import lxml.html
import csv
import re
from lxml import etree
from lxml import html

#this will write the data scarped into csv format with file name test.scv in same folder
with open('test.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    url = []
    #loop
    for x in range(1,135):

            a = "http://gympp.com/ncr/"+str(x)
            url.append(a)
            print a

            response = requests.get(a)
            html = response.content
            item = etree.HTML(html)
            name = item.xpath('//*[@class="product_name"]/div/a/@href')
            print name        
            for x in name:
                    b = "http://gympp.com"+x
                    url.append(b)
                    print b
                    response = requests.get(b)
                    html = response.content
                    item = etree.HTML(html)
                    name = item.xpath('//*[@class="prod-name"]/text()')
                    location = item.xpath('//*[@class="text"]/ul/li/text()')
                    contact = item.xpath('//*[@class="text"]/ul/li/span/text()')
                    
                    for x in range(0,len(name)):
                    
                            row = [(name[x].strip()).encode('ascii','ignore')]+[(location[x].strip()).encode('ascii','ignore')]+[(contact[x].strip()).encode('ascii','ignore')]
                            print row
                            spamwriter.writerow(row)
