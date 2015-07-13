"""
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
 ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で
見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
コーパス中で頻出する述語と格パターンの組み合わせ
「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""

import subprocess
from lxml import etree as ET
from collections import defaultdict


def get_reputation(xml):
    reputation = defaultdict(list)
    f = open('data/45_result.txt', 'w')
    for sentence in xml.findall('.//sentence'):
        sentence_id = sentence.attrib['id']
        for chunk in sentence:
            link = chunk.attrib['link']
            for tok in chunk:
                feature = tok.attrib['feature'].strip().split(',')
                part = feature[0]
                if link == '-1':
                    break
                if part == '動詞':
                    verb_word = feature[-3]
                    res = get_next_chunk(sentence_id, link, part)
                    if res is None:
                        break
                    particle_word = res
                    reputation[verb_word].append(particle_word)
    for key, value in reputation.items():
        value.sort()
        f.write(key + '\t' + ' '.join(value) + '\n')
    f.close()


def get_next_chunk(sentence_id, link_id, ex_part):
    sentence = xml.find(".//sentence[@id='%s']" % sentence_id)
    chunk = sentence.find(".//chunk[@id='%s']" % link_id)
    for tok in chunk:
        feature = tok.attrib['feature'].strip().split(',')
        if feature[0] == '助詞':
            return tok.text

if __name__ == '__main__':
    # Optimize: more faseter
    xml = ET.parse('data/neko.xml')
    get_reputation(xml)
    cmd = 'grep -e "^する" -e "^見る" -e "^与える" {0} | sed -e "s/\\s/\\n/g" |uniq -c | sort -r -n -k1'.format('data/45_result.txt')
    subprocess.call(cmd, shell=True)
