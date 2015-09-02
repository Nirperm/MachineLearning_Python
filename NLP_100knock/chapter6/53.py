"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('data/nlp.xml')
    root = tree.getroot()
    words = root.findall('./document/sentences/sentence/tokens/token/word')

    for word in words:
        print(word.text)
