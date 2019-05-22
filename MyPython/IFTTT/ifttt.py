import requests
from stock import get_stock
import time

key = 'eW75mPiKXppT9gg6MyLTPojWPkZU-qIRiSzRHdcP75z'  # your IFTTT web hook key
event_name = 'line'    # your IFTTT event name


def send_ifttt(v1):
    url = ('https://maker.ifttt.com/trigger/' + event_name + '/with/key/' + key +
           '?value1=' + str(v1))
    r = requests.get(url)  # send HTTP GET ,and get response
    if r.text[:5] == "Congr":
        print('already send (' + str(v1) + ') to Line')
    else:
        print("fail")
    return r.text


if __name__ == "__main__":
    msg = "<br>資工2B<br>夏靖傑<br>406410414<br><br>\n"  # line ifttt msg <br> = \n

    stock_codes = ['3010', '2340', '2337']
    for code in stock_codes:
        print('get')
        msg += get_stock(code) + '<br>'
        time.sleep(5)

    ret = send_ifttt(msg)  # send HTTP request to IFTTT
    print('IFTTT response：', ret)

