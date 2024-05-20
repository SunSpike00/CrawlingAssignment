import requests
import time
from bs4 import BeautifulSoup

def genieChart(code):
  header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
  request = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20240520&hh=12&rtm=Y&pg={0}'.format(code), headers=header)
  soup = BeautifulSoup(request.text)

  rank = soup.find("td", {'class':'number'})
  titles = soup.findAll("a", {'class':'title ellipsis'})
  artists = soup.findAll("a", {'class':'artist ellipsis'})
  
  rank.find("span", attrs={"class":"rank"}).decompose()
  rank = int(rank.text.strip())

  for i, (t, a) in enumerate(zip(titles, artists)):
    title = t.text.strip()
    artist = a.text.strip()
    print('{0:3d}위, {1:s} - {2:s}'.format(i+rank, title, artist))

for i in range(1, 5):
  genieChart(i)
  time.sleep(1)