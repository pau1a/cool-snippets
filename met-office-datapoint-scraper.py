import lxml
from bs4 import BeautifulSoup
import urllib.request
codes={'NA':'Not available','0': 'Clear night','1': 'Sunny day','2': 'Partly cloudy (night)','3': 'Partly cloudy (day)','4': 'Not used','5': 'Mist','6': 'Fog','7': 'Cloudy','8': 'Overcast','9': 'Light rain shower (night)','10': 'Light rain shower (day)','11': 'Drizzle','12': 'Light rain','13': 'Heavy rain shower (night)','14': 'Heavy rain shower (day)','15': 'Heavy rain','16': 'Sleet shower (night)','17': 'Sleet shower (day)','18': 'Sleet','19': 'Hail shower (night)','20': 'Hail shower (day)','21': 'Hail','22': 'Light snow shower (night)','23': 'Light snow shower (day)','24': 'Light snow','25': 'Heavy snow shower (night)','26': 'Heavy snow shower (day)','27': 'Heavy snow','28': 'Thunder shower (night)','29': 'Thunder shower (day)','30': 'Thunder'}
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
