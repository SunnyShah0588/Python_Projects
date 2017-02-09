import requests
from bs4 import BeautifulSoup

def web_clawer(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://cyro.se/episodes/index.php?&page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        #print(soup)
        for link in soup.findALL('td', {'target': '_self'}):
            href = "http://cyro.se" + link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1

print("hi")
web_clawer(1)
print("hi")

