import requests
from bs4 import BeautifulSoup
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}
rs = requests.session()
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)
response = rs.get("https://www.ptt.cc/bbs/Gossiping/index.html")
print(response.status_code)
root = BeautifulSoup(response.text, "html.parser")
links = root.find_all("div", class_="title")
for link in links:
    print(link.a["href"])
for link in links:
    page_url = "https://www.ptt.cc"+link.a["href"]
    print(page_url)
response = rs.get(page_url)
result = BeautifulSoup(response.text, "html.parser")
result
