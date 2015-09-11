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


from section_41 import make_text_chunk


def get_verb_frame(text_chunk_list):
    particle = '助詞'
    verb = '動詞'
    get_pattern_flag = False
    for sentence_chunk_list in text_chunk_list:
        for chunk in sentence_chunk_list:
            get_pattern_flag = False
            particle_phrase = ''
            particle_words = ''
            for num in chunk.srcs:
                num = int(num)
                if chunk.check_phrase_pos(verb) and sentence_chunk_list[num].check_phrase_pos(particle):
                    particle_words += str(sentence_chunk_list[num].get_pos_word(particle))
                    particle_phrase += sentence_chunk_list[num].get_phrase()
                    particle_phrase += ' '
                    get_pattern_flag = True
            if get_pattern_flag:
                print(chunk.get_pos_word(verb), '\t', particle_words, '\t', particle_phrase)

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_verb_frame(text_chunk_list)
