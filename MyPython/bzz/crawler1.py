import requests
from bs4 import BeautifulSoup
import time

rq = requests.get("https://www.ptt.cc/bbs/ClashRoyale/index406.html")
sp = BeautifulSoup(rq.text, "html.parser")
sel = sp.select("div.title a")
for s in sel:
    fp = open('file.txt', 'w')
    fp.write(str(s["href"]) + sp.text + "\n")
fp.close()

f = open('file.txt', 'r')
r = f.read()
print(r)
f.close()
