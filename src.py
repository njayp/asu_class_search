import requests
from bs4 import BeautifulSoup

URL = 'https://webapp4.asu.edu/catalog/myclasslistresults?t=2207&s=CSE&n=5*&hon=F&promod=F&c=TEMPE&e=all&page=1'
watchlist = ["76954", "95355"]

soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
resultset = soup.find_all(attrs={'class':'classNbrColumnValue'})
for result in resultset:
    if result.text.strip() in watchlist:
        print(result.parent.find(attrs={'class':'col-xs-3'}).text.strip())
