import requests
import pandas as pd
from bs4 import BeautifulSoup

r = requests.get('https://www.golfdigest.com/gallery/americas-100-greatest-golf-courses-ranking')

soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'listicle-item'})

records = []
for result in results:
    name = result.find('strong').text
    description = result.find('div', attrs={'class': 'listicle-caption'}).text
    records.append((name, description))

df = pd.DataFrame(records, columns=['Course Name', 'Description'])
df = df.to_csv('Top-100-2019.csv', index=False, encoding='utf-8')
