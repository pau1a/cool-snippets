import lxml
from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/3136?res=3hourly&key=---your API KEY here---") as url:
    s = url.read()

y=BeautifulSoup(s, "lxml")

brian=y.findAll('rep') #captures all reports from xml and adds them to a list called brian

for elem in brian: #print out list brian on separate lines
    print (elem)
