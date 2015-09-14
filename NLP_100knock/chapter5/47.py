"""
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」
という文から，以下の出力が得られるはずである．

返事をする      と に は        及ばんさと 手紙に 主人は
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語（サ変接続名詞+を+動詞）
コーパス中で頻出する述語と助詞パターン
"""


from section_41 import make_text_chunk


# FIXME: a little bugy, now result is 返事をする > さ と は に を  > 及ばんさと 主人は 手紙に--


def get_functional_verb_frame(text_chunk_list):
    verb = '動詞'
    particle = '助詞'
    pos1 = 'サ変接続'
    for sentence_chunk_list in text_chunk_list:
        get_pattern_flag = False
        sahen_flag = False
        for chunk in sentence_chunk_list:
            get_pattern_flag = False
            particle_phrase = ''

            particle_words = ''
            for num in chunk.srcs:
                num = int(num)
                if chunk.check_phrase_pos(verb) and sentence_chunk_list[num].check_phrase_pos(particle):
                    temp_phrase = sentence_chunk_list[num].get_phrase()
                    if sentence_chunk_list[num].check_phrase_pos1(pos1) and sentence_chunk_list[num].check_phrase_word('を'):
                        sahen_phrase = temp_phrase
                        sahen_flag = True
                    else:
                        particle_phrase += temp_phrase
                    particle_words += str(sentence_chunk_list[num].get_pos_word(particle))
                    particle_phrase += ' '

                    get_pattern_flag = True
            if get_pattern_flag and sahen_flag:
                print(sahen_phrase + chunk.get_pos_word(verb), '\t', particle_words, '\t', particle_phrase)

if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    get_functional_verb_frame(text_chunk_list)
