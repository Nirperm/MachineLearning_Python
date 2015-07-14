"""
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た

"""


import CaboCha


def treeparse(sentence):

    tree = c.parse(sentence)
    size = tree.size()

    own_id = 0
    phrase_list = []
    phrase = ''
    phrase_id = 0
    phrase_link = 0
    dependency_particle = 0
    case_particle = 0
    subj = ''
    obj = ''
    pred = ''

    for i in range(0, size):
        token = tree.token(i)

        if token.chunk:
            if (phrase != ''):
                phrase_list.append((phrase, phrase_id, phrase_link, dependency_particle, case_particle))  # 前の句をリストに追加
            dependency_particle = 0
            case_particle = 0
            word = token.normalized_surface
            word_id = own_id
            word_link = token.chunk.link
            own_id += 1
        else:
            word += token.normalized_surface
        feature = (token.feature).split(',')
        if (feature[1] == '係助詞'):
            dependency_particle = 1
        if (feature[1] == '格助詞'):
            case_particle = 1

        phrase_list.append((word, word_id, word_link, dependency_particle, case_particle))  # 最後にも前の句をリストに追加

    for word_chunk in phrase_list:
        # print(k[1], k[0], k[2], k[3], k[4])
        if (word_chunk[2] == -1):  # link == -1
            pred_id = word_id  # この時のidを覚えておく
    """
    print('--------')
    print('述語句')
    """
    for k in phrase_list:
        if (word_chunk[1] == pred_id):  # pred_idと同じidを持つ句を探す
            pass
            # print(k[1], k[0], k[2], k[3], k[4])
    """
    print('--------')
    print('述語句に係る句')
    """
    for word_chunk in phrase_list:
        if (word_chunk[2] == pred_id):  # pred_idと同じidをリンク先に持つ句を探す
            pass
            # print(k[1], k[0], k[2], k[3], k[4])
    """
    print('--------')
    print('その中から、主語句と目的語句を選ぶ')
    """
    for word_chunk in phrase_list:
        if (word_chunk[2] == pred_id):  # pred_id と同じidをリンク先に持つ句を探す
            if (word_chunk[3] == 1):
                subj = word_chunk[0]
                # subj += ' -> ' + word_chunk[0]
            if (word_chunk[4] == 1):
                obj = word_chunk[0]
                # obj += ' -> ' + word_chunk[0]
        if (word_chunk[1] == pred_id):
                pred = word_chunk[0]
                # pred += ' -> ' + word_chunk[0]

    return (subj + ' -> ' + obj + ' -> ' + pred + '\n')


if __name__ == '__main__':
    c = CaboCha.Parser()
    f = open('data/neko.txt', encoding='utf-8')
    content = f.read()
    f.close()

    result = ''
    sentence = content.split('。')
    for line in sentence:
        if (line != ''):
            cabocha_answer = treeparse(line)

        if (result == ''):
            result = cabocha_answer
        else:
            result += cabocha_answer

    print(result)
