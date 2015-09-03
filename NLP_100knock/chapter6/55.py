"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""

import xml.etree.ElementTree as ET


if __name__ == '__main__':
    tree = ET.parse('data/nlp.xml')
    root = tree.getroot()
    tokens = root.findall('.//token')

    for token in tokens:
        if 'PERSON' == token.find('NER').text:
            print(token.find('word').text)
