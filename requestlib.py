import requests
r = requests.get('https://api.github.com/events')
r.text # Shows api text format | >> u'[{"repository":{"open_issues":0,"url":"https://github.com/...
r.encoding # Yazým Stilini gösterir | 'utf-8'
r.content # Api Ýçeriðini Gösterir
r.json() # Api JavaScript Dosyalarýný Çeker
r.raw # Raw Fomratýnda Oluþturur
r.url # Site Adresini Gösterir | 'https://github.com/'
r.status_code # Site Statü Durumu

# Yapýlabilir Kodlar

url = 'https://api.github.com/some/endpoint'#input getirilebilir
headers = {'user-agent': 'my-app/0.0.1'} # seçenekler elif ile ayarlanabilir
r = requests.get(url, headers=headers) # Tarama Yapar

# Dosya Çýkarma
url = 'https://httpbin.org/post' #Adres
files = {'file': open('report.xls', 'rb')} # Ýstenilen Dosya

r = requests.post(url, files=files) # Dosyayý Çeker
r.text #Text Formatýnda Çýkartýr

# Response Statü Kodlarý
r = requests.get('https://httpbin.org/get') # Website Adresi
r.status_code # Statü Durumunu Gösterir | >> 200

r.status_code == requests.codes.ok # Iki Komut Aynýdýr
r.raise_for_status() # Eðer hata alýnýrsa bu kod denenmeli -> Aþþaðýda

#---
bad_r = requests.get('https://httpbin.org/status/404')
bad_r.status_code # Hata Kodunu Gösterir
#Alýnacak Hata >>

#Traceback (most recent call last):
#  File "requests/models.py", line 832, in raise_for_status
#    raise http_error
#requests.exceptions.HTTPError: 404 Client Error

# Çözümü | r.raise_for_status()

#---
# Server Headers
r.headers # Sunucu Python Baþlýklarýný Gösterir 

# Örnek =>
#{
#    'content-encoding': 'gzip',
#    'transfer-encoding': 'chunked',
#    'connection': 'close',
#    'server': 'nginx/1.0.4',
#    'x-runtime': '148ms',
#    'etag': '"e1ca502697e5c9317743dc078f67693f"',
#    'content-type': 'application/json'
#}
r.headers['Content-Type'] #Bu Þekilde Istenilen Ýçerikte Apiden Çekilebilir

r.headers == r.headers.get # Iki komut aynýdýr


#---

#Siteden Çerez Çekme
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

r.cookies['example_cookie_name'] ## Çerez Adý

# Geliþmiþ Çerez Çekimi
url = 'https://httpbin.org/cookies' # url yerine input ekleyip site adresi koyma
cookies = dict(cookies_are='working') # If Elif ile çeþitlendirilebilir cookies seçim ekraný

r = requests.get(url, cookies=cookies)
r.text #Yazý Formatýnda Çýkartýr

#----------------------------------------------------#

from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content)) # Api'deki resimlere bakar