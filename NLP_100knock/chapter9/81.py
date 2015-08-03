"""
81. 複合語からなる国名への対処
英語では，複数の語の連接が意味を成すことがある．
例えば，アメリカ合衆国は"United States"，
イギリスは"United Kingdom"と表現されるが，
"United"や"States"，"Kingdom"という単語だけでは，
指し示している概念・実体が曖昧である．
そこで，コーパス中に含まれる複合語を認識し，
複合語を1語として扱うことで，複合語の意味を推定したい．
しかしながら，複合語を正確に認定するのは大変むずかしいので，
ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，
80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．例えば，"United States"は"United_States"，
"Isle of Man"は"Isle_of_Man"になるはずである．
"""


import urllib.request as req
from bs4 import BeautifulSoup

response = req.urlopen('http://www6.kaiho.mlit.go.jp/isewan/image/flags/_flags.htm')
body = response.read()
soup = BeautifulSoup(body)

country_names = []
for i, tr in enumerate(soup.find_all('tr')):
    if i == 1:
        country_names.append(tr.findChildren()[4].text)
    else:
        country_names.append(tr.findChildren()[3].text)

while '略号' in country_names:
    country_names.remove('略号')
