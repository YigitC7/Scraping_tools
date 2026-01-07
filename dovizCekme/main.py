# Yazan Yiğit Çıtak

import requests
from bs4 import BeautifulSoup
from os import system, name
from time import sleep

class scraping:
    def __req(url):
        respnse = requests.get(url=url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"})
        
        if respnse.status_code != 200:
            return respnse.status_code

        return respnse.text
    
    def __ayikla(html,value):
        if isinstance(html, int):return html

        soup = BeautifulSoup(html,"html.parser")

        ayiklama = soup.find_all("span",attrs={"class":"value","data-socket-key":value})
        
        icerik = []

        for data in ayiklama:
            icerik.append(data.get_text(strip=True))
        
        return icerik[0]
    
    def get(value):
        html = scraping.__req("https://www.doviz.com/")
        
        return scraping.__ayikla(html,value)
    
# Value Girişleri: gram-altin USD EUR GBP XU100 d-bitcoin gumus BRENT 

def shell():
    if name == "nt":
        clearCommand = "cls"
    elif name == "posix":
        clearCommand = "clear"

    while True:
        try:
            yenilenmeSuresi = int(input("Yenilenme Süresi Belirle (Saniye) >"))
            break
        except ValueError:
            print("Lütfen Saniye girin")

    while True:
        printDoviz = f"""|Kaynak: doviz.com\n|Geliştirici: github.com/yigitc7\n[Çıkış için CTR + Z]\n\n|Dolar : {scraping.get("USD")}| |Gram Altın : {scraping.get("gram-altin")}| |EURO : {scraping.get("EUR")}|"""
        system(clearCommand)
        print(printDoviz)
        sleep(yenilenmeSuresi)
        print("\n[Yenileniyor ...]")
        sleep(0.5)

if __name__ == "__main__":shell()
