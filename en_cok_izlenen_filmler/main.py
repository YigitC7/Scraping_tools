# Yazan Yiğit Çıtak

import requests
from bs4 import BeautifulSoup

def request(url="https://www.imdb.com/list/ls088323918/"):
    response = requests.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"})
    return response.text

def html_ayikla(html=request()):
    soup = BeautifulSoup(html,"html.parser")
    datas = soup.find_all("h3",attrs={"class":"ipc-title__text"})

    icerik = []

    for data in datas:
        icerik.append(data.get_text(strip=True))
    
    return icerik

def data_show():
    veri = html_ayikla()
    for i in veri:
        print(i)

if __name__ == "__main__":
    print("Sinemada en çok izlenen Türkiye yapımı filmler:")
    data_show()
