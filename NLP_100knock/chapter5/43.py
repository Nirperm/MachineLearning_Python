"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""

import CaboCha
import xml.etree.ElementTree as ET
from collections import defaultdict


def get_reputation(xml):
    flag = None
    reputation = defaultdict(str)

    for el in xml.findall('.//chunk'):
        tok = el.find('tok')
        feature = tok.attrib['feature'].strip().split(',')
        part = feature[0]
        typ = feature[1]

        if part == '名詞' and \
            (typ == '一般' or typ ==' 固有名詞'):
                reputation['object'] = tok.text
        if part == '形容詞':
            reputation['adjective'] = feature[6]
        link = el.attrib['link']
        if link == '-1':
            break
        while 1:
            res = get_next_chunk(link, part)
            if res is None:
                break
            part, typ, word, link = res

            if part == '名詞' and \
                (typ == '一般' or typ == '固有名詞'):
                reputation['object'] = word
            if part == '形容詞':
                reputation['adjective'] = word
                if reputation['object'] is not None:
                    flag = 1
                    break
        if flag == 1:
            break

    print(reputation['object'] + '\t' + reputation['adjective'])


def get_next_chunk(linkid, ex_part):
    if linkid == '-1':
        return None
    this_chunk = xml.find(".//chunk[@id='%s']" % linkid)
    link = this_chunk.attrib['link']

    tok = this_chunk.find('tok')
    feature = tok.attrib['feature'].strip().split(',')
    if ex_part == '名詞':
        if feature[0] == '名詞':
            return feature[0], feature[1], tok.text, link
        elif feature[0] == '動詞' or feature[0] == '形容詞':
            return feature[0], feature[1], feature[6], link
    elif ex_part == '動詞':
        if feature[0] == '名詞':
            return feature[0], feature[1], tok.text, link
    elif ex_part == '形容詞':
        if feature[0] == '名詞':
            return feature[0], feature[1], tok.text, link

if __name__ == '__main__':
    c = CaboCha.Parser()
    f = open('data/neko.txt', encoding='utf-8')
    content = f.read()
    f.close

    tree = c.parse(content)
    xml = ET.fromstring(tree.toString(CaboCha.FORMAT_XML))
    get_reputation(xml)
