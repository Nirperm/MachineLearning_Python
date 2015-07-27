"""
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを

"""

from lxml import etree as ET
from collections import defaultdict


def get_reputation(xml):
    reputation = defaultdict(list)
    origin = defaultdict(list)
    # f = open('data/46_result.txt', 'w')
    for sentence in xml.findall('.//sentence'):
        sentence_id = sentence.attrib['id']
        for chunk in sentence:
            link = chunk.attrib['link']
            print(link)
            for tok in chunk:
                feature = tok.attrib['feature'].strip().split(',')
                part = feature[0]
                """
                if part == '動詞':
                    verb_word = feature[-3]
                """
                """
                print(sentence_id + '\t' + link + '\t' + tok.text)
                origin[sentence_id].append({link: tok.text})
                print(sorted(origin.items()))
                """
                # res = get_next_chunk(sentence_id, link, part)


def get_next_chunk(sentence_id, link_id, ex_part):
    if link_id == '-1':
        return None
    sentence = xml.find(".//sentence[@id='%s']" % sentence_id)
    chunk = sentence.find(".//chunk[@id='%s']" % link_id)
    tok_list = chunk.findall(".//tok")
    print([x.text for x in tok_list])
    # print([x for x in tok_list if x.attrib[""]])


if __name__ == '__main__':
    # Optimize: more faseter
    xml = ET.parse('data/neko8.xml')
    get_reputation(xml)
