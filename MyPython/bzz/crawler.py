import requests
from bs4 import BeautifulSoup
import tkinter as tk
q = 0
a = []
i = 0
z= 0
name = open("name.txt", "w", encoding='utf-8')
p = requests.Session()
url = requests.get("http://www.csie.tku.edu.tw/members/teacher.php?class=110")
url.encoding = 'utf-8'
soup = BeautifulSoup(url.text, "html.parser")
data = soup.select("div.teacher_left")
sel = soup.select("div.pic img")
sel2 = soup.select("div.info li")
for b in sel2:
    print(sel2[0+i].text.lstrip("職稱: "))
    print(sel2[1 + i].text.lstrip("姓名: "))
    name.write(sel2[i].text.lstrip("職稱: ") + "  " + sel2[1 + i].text.lstrip("姓名: ") + "\n")
    a.append(sel2[i].text.lstrip("職稱: ") + "  " + sel2[1 + i].text.lstrip("姓名: "))
    i += 4
    if i>len(sel2)-4:
        i=0
name.close()
for c in sel:
    pic = requests.get(c["src"])
    img = pic.content
    pic_out = open("teacherphoto/"+str(a[q]), 'wb')
    pic_out.write(img)
    pic_out.close()
    q += 1

if __name__ == '__main__':

    root = tk.Tk()
    root.title('crawler')
    root.geometry("1200x600")    # window size
    root.config(background="#262626")

    listbox = tk.Listbox(root, font=("Arial", 14), width=500,height=600, background="#262626", foreground="white")
    listbox.pack()
    for c in sel:
        listbox.insert(tk.END,a[z]+c["src"]+"\n")
        z=z+1

    root.mainloop()