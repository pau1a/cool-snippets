import lxml
from bs4 import BeautifulSoup
import urllib.request
codes={'NA':'Not available','0': 'Clear night','1': 'Sunny day','2': 'Partly cloudy (night)','3': 'Partly cloudy (day)','4': 'Not used','5': 'Mist','6': 'Fog','7': 'Cloudy','8': $
final=[]

with urllib.request.urlopen("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/3136?res=3hourly&key=3a169d7f-320c-40f6-8ffb-2078e513b24d") as url:
    s = url.read()

y=BeautifulSoup(s, "lxml")
y=str(y)
weather_report=[element.strip('<>') for element in y.split('<')]

for item in weather_report:
    if 'rep d' in item:
        final.append(item.split(' ')[-1])
weather=final[1].split('"')[1]

print(codes[weather])
