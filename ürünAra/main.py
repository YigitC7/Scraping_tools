# Yazan Yiğit Çıtak

import requests
from bs4 import BeautifulSoup

class UrunListele:   
    def listele(urunAdi):
        return UrunListele.__htmlAyiklamaTool(UrunListele.__request(urunAdi))
    
    def __request(product):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
        google_product_get_url = f"https://www.pazarama.com/arama?q={product}"
        
        response = requests.get(google_product_get_url,headers=header)

        return response.text

    def __htmlAyiklamaTool(html):
        soup = BeautifulSoup(html,"html.parser")
        class Data:
            def datas(index=5):
                fiyat = ["div",{"class":"text-gray-600 text-xl font-semibold leading-tight"}]
                isim = ["h2",{"class":"text-xs text-gray-600 font-normal line-clamp-2 h-8 text-xs leading-4 mb-1.5"}]
                
                fiyat_get = Data.__veriAyikla(finds=fiyat,index=index) 
                isim_get = Data.__veriAyikla(finds=isim,index=index)

                icerik = {}
                
                for Loopindex in range(index):
                    icerik[isim_get[Loopindex]] = fiyat_get[Loopindex]

                return icerik

            def __veriAyikla(finds,index):
                index_start = 0

                div_icerik = soup.find_all(finds[0],attrs=finds[1])
                icerik = []
        
                for div in div_icerik:
                    index_start += 1
                    icerik.append(div.get_text(strip=True))

                    if index_start == index:
                        break
                
                return icerik
            
        return Data.datas()
   



