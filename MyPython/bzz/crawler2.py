import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/ClashRoyale/index.html"
for i in range(3):
    rq = requests.get(url)
    sp = BeautifulSoup(rq.text, "html.parser")
    sel = sp.select("div.title a")
    for s in sel:
        print(s["href"], s.text)
    u = sp.select("div.btn-group.btn-group-paging a")  # a標籤
    print("本頁的URL為" + url)
    url = "https://www.ptt.cc" + u[1]["href"]  # 上一頁的網址
