"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，
単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('data/nlp.xml')
    root = tree.getroot()
    tokens = root.findall('.//token')

    for token in tokens:
        word = token.find('word').text
        lemma = token.find('lemma').text
        pos = token.find('POS').text

        print('\t'.join([word, lemma, pos]))
