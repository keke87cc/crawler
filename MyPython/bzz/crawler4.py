import requests

pic = requests.get('https://imgur.dcard.tw/N2k5kV2m.jpg')
img2 = pic.content
pic_out = open('img1.png', 'wb')
pic_out.write(img2)
pic_out.close()