"""
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

import CaboCha
import pydot


def get_word(tree, chunk):
    surface = ''  # if 一ファイルに全ての要素がかけていなかったらlistにする
    for i in range(chunk.token_pos, chunk.token_pos + chunk.token_size):
        token = tree.token(i)
        features = token.feature.split(',')
        if features[0] == '名詞':
            surface += token.surface
        elif features[0] == '形容詞' or '動詞':
            surface += features[6]
            break
        elif features[0] == '副詞' or '接頭詞' or '接続詞' or '連体詞':
            surface += features[6]
            break
        elif features[0] == '記号' or '助詞' or '助動詞':
            break
    return surface


def get_2word(tree):
    chunk_dic = {}
    chunk_id = 0
    for i in range(0, tree.size()):
        token = tree.token(i)
        if token.chunk:
            chunk_dic[chunk_id] = token.chunk
            chunk_id += 1
    tuples = []
    for chunk_id, chunk in chunk_dic.items():
        if chunk.link > 0:
            from_surface = get_word(tree, chunk)
            to_chunk = chunk_dic[chunk.link]
            to_surface = get_word(tree, to_chunk)
            print(from_surface)
            print(to_surface)
            tuples.append((from_surface, to_surface))
    return tuples


if __name__ == '__main__':
    """
    c = CaboCha.Parser()
    f = open('data/neko.txt', encoding='utf-8')
    content = f.read().split('\n')
    f.close()
    for e in content:
        print(e)
    # tree = c.parse(content)
    """

    """
    with open('data/neko.txt', encoding='utf-8') as f:
        for line in f:
            tree = c.parse(line)
            edges = get_2word(tree)
            graph = pydot.graph_from_edges(edges)
            graph.write_png('data/neko_cabocha.png', prog='dot')
    """
