import requests
from bs4 import BeautifulSoup

site="https://www.brainyquote.com/quote_of_the_day"
result = requests.get(site)
result = result.content

soup = BeautifulSoup(result,"html.parser")
imgs = soup.find_all("img")

# grabs the alt text from the img and gets everything before the author
quote = imgs[1].get('alt', '').split(' -')

print(quote[0])
file = open('daily_quote.txt','w')
file.write(quote[0] + "\n")
file.close()
