"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""

# import CaboCha
from lxml import etree as ET
# from collections import defaultdict


def reshape(input_file):
    """ Add root tag due to can not use cabocha xml output without change """
    f = open('data/neko.xml', 'w')
    f.write('<root>\n')
    with open(input_file, encoding='utf-8') as xml:
        sentenceid = 0
        for line in xml:
            if line.find('<sentence>') > -1:
                f.write('<sentence id="' + str(sentenceid) + '">\n')
                sentenceid += 1
            else:
                if line.find('&') > 0 or line.find('</tok>') == 0:
                    continue
                else:
                    f.write(line)
    f.write('</root>')
    f.close()


def get_reputation(xml):
    # reputation = defaultdict(list)
    for sentence in xml.findall('.//sentence'):
        sentence_id = sentence.attrib['id']
        for chunk in sentence:
            link = chunk.attrib['link']
            for tok in chunk:
                feature = tok.attrib['feature'].strip().split(',')
                part = feature[0]
                if link == '-1':
                    break
                if part == '名詞':
                    noun_word = tok.text
                    res = get_next_chunk(sentence_id, link, part)
                    if res is None:
                        break
                    verb_word = res
                    print(noun_word + '\t' + verb_word)

                    # In case of saving extracted word
                    """
                    reputation['object'].append(noun_word)
                    reputation['verb'].append(verb_word)

    reputation_dict = dict(zip(reputation['object'], reputation['verb']))
    for key, value in reputation_dict.items():
        print(key + '\t' + value)
    """


def get_next_chunk(sentence_id, linkid, ex_part):
    sentence = xml.find(".//sentence[@id='%s']" % sentence_id)
    chunk = sentence.find(".//chunk[@id='%s']" % linkid)
    for tok in chunk:
        feature = tok.attrib['feature'].strip().split(',')
        if feature[0] == '動詞':
            return tok.text

if __name__ == '__main__':
    # Optimize: more faseter
    # reshape('data/neko.txt.cabocha.xml') In case of utlizing unchanged form Cabocha XML output
    xml = ET.parse('data/neko.xml')
    get_reputation(xml)

    # In case of utlizing of Cabocha
    """
    c = CaboCha.Parser()
    f = open('data/neko.txt', encoding='utf-8')
    content = f.read()
    f.close

    tree = c.parse(content)
    xml = ET.fromstring(tree.toString(CaboCha.FORMAT_XML))
    get_reputation(xml)
    """
