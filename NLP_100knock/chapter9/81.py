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
80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．
例えば，"United States"は"United_States"，
"Isle of Man"は"Isle_of_Man"になるはずである．
"""


import os
import re
import urllib.request as req
from bs4 import BeautifulSoup


def get_countries():
    response = req.urlopen('http://www6.kaiho.mlit.go.jp/isewan/image/flags/_flags.htm')
    body = response.read()
    soup = BeautifulSoup(body)

    country_names = []
    for i, tr in enumerate(soup.find_all('tr')):
        if i == 1:
            country_names.append(tr.findChildren()[4].text)
        elif tr.findChildren()[3].text == '略号':
            pass
        else:
            country_names.append(tr.findChildren()[3].text)

        f = open('data/countries.txt', 'w')
        for country in country_names:
            f.write(country + '\n')
        f.close()
    return country_names


def make_trans_dict(country_names):
    trans_dict = {}
    for country in country_names:
        for char in country:
            if char in ' ':
                trans_dict[country] = country.replace(' ', '_')
    return trans_dict


def read_coupus():
    with open('data/tokenaize-enwiki-20150112-400-r100-10576.txt') as f:
        texts = f.read()
    return texts


def multi_replace(text, dic):
    r = re.compile('|'.join(dic))

    def dedictkey(text):
        for key in dic.keys():
            if re.search(key, text):
                return key

    def one_xlat(match):
        return dic[dedictkey(match.group(0))]

    return r.sub(one_xlat, text)


if __name__ == '__main__':
    if os.path.isfile('data/countries.txt') is False:
        country_names = get_countries()
    else:
        with open('data/countries.txt', encoding='utf-8') as f:
            country_names = f.readlines()
        country_names = [country.strip() for country in country_names]

    trans_dict = make_trans_dict(country_names)
    texts = read_coupus()
    result = multi_replace(texts, trans_dict)
    with open('data/81_result.txt', 'w') as f2:
        f2.write(result)
