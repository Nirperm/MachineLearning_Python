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

import subprocess
from section_41 import make_text_chunk


def get_case_pattern(text_chunk_list):
    particle = '助詞'
    verb = '動詞'
    f = open('data/45_result.txt', 'w')
    get_pattern_flag = False
    for sentence_chunk_list in text_chunk_list:
        for chunk in sentence_chunk_list:
            get_pattern_flag = False

            particle_words = ''
            for num in chunk.srcs:
                num = int(num)
                if chunk.check_phrase_pos(verb) and sentence_chunk_list[num].check_phrase_pos(particle):
                    particle_words += str(sentence_chunk_list[num].get_pos_word(particle))
                    get_pattern_flag = True
            if get_pattern_flag:
                f.write(chunk.get_pos_word(verb) + '\t' + particle_words + '\n')
    f.close()

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_case_pattern(text_chunk_list)
    cmd = 'grep -e "^する" -e "^見る" -e "^与える" {0} | sed -e "s/\\s/\\n/g" |uniq -c | sort -r -n -k1'.format('data/45_result.txt')
    print(subprocess.call(cmd, shell=True))
