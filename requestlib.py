import requests
r = requests.get('https://api.github.com/events')
r.text # Shows api text format | >> u'[{"repository":{"open_issues":0,"url":"https://github.com/...
r.encoding # Yaz�m Stilini g�sterir | 'utf-8'
r.content # Api ��eri�ini G�sterir
r.json() # Api JavaScript Dosyalar�n� �eker
r.raw # Raw Fomrat�nda Olu�turur
r.url # Site Adresini G�sterir | 'https://github.com/'
r.status_code # Site Stat� Durumu

# Yap�labilir Kodlar

url = 'https://api.github.com/some/endpoint'#input getirilebilir
headers = {'user-agent': 'my-app/0.0.1'} # se�enekler elif ile ayarlanabilir
r = requests.get(url, headers=headers) # Tarama Yapar

# Dosya ��karma
url = 'https://httpbin.org/post' #Adres
files = {'file': open('report.xls', 'rb')} # �stenilen Dosya

r = requests.post(url, files=files) # Dosyay� �eker
r.text #Text Format�nda ��kart�r

# Response Stat� Kodlar�
r = requests.get('https://httpbin.org/get') # Website Adresi
r.status_code # Stat� Durumunu G�sterir | >> 200

r.status_code == requests.codes.ok # Iki Komut Ayn�d�r
r.raise_for_status() # E�er hata al�n�rsa bu kod denenmeli -> A��a��da

#---
bad_r = requests.get('https://httpbin.org/status/404')
bad_r.status_code # Hata Kodunu G�sterir
#Al�nacak Hata >>

#Traceback (most recent call last):
#  File "requests/models.py", line 832, in raise_for_status
#    raise http_error
#requests.exceptions.HTTPError: 404 Client Error

# ��z�m� | r.raise_for_status()

#---
# Server Headers
r.headers # Sunucu Python Ba�l�klar�n� G�sterir 

# �rnek =>
#{
#    'content-encoding': 'gzip',
#    'transfer-encoding': 'chunked',
#    'connection': 'close',
#    'server': 'nginx/1.0.4',
#    'x-runtime': '148ms',
#    'etag': '"e1ca502697e5c9317743dc078f67693f"',
#    'content-type': 'application/json'
#}
r.headers['Content-Type'] #Bu �ekilde Istenilen ��erikte Apiden �ekilebilir

r.headers == r.headers.get # Iki komut ayn�d�r


#---

#Siteden �erez �ekme
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

r.cookies['example_cookie_name'] ## �erez Ad�

# Geli�mi� �erez �ekimi
url = 'https://httpbin.org/cookies' # url yerine input ekleyip site adresi koyma
cookies = dict(cookies_are='working') # If Elif ile �e�itlendirilebilir cookies se�im ekran�

r = requests.get(url, cookies=cookies)
r.text #Yaz� Format�nda ��kart�r

#----------------------------------------------------#

from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content)) # Api'deki resimlere bakar