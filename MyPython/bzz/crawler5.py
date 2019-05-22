import requests
from bs4 import BeautifulSoup
fp = open('test.txt', 'w')
rs = requests.Session()
rq = requests.get("https://www.dcard.tw/f/pet")
sp = BeautifulSoup(rq.text, "html.parser")
sel = sp.select("div.PostList_entry_1rq5Lf a.PostEntry_root_V6g0rd")
a = []
for s in sel:
    print(s["href"]+"\n")
    a.append("https://www.dcard.tw" + s["href"])
    fp.write("https://www.dcard.tw"+s["href"]+"\n")
fp.close()

