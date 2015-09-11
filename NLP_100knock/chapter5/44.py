"""
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

from section_41 import make_text_chunk
import pygraphviz as pgv


def draw_graph(text_chunk_list):
    graph = pgv.AGraph(strict=True, directed=True)
    count = 0
    for sentence_chunk_list in text_chunk_list:
        count += 1
        for chunk in sentence_chunk_list:
            if chunk.dst != '-1':
                from_word = str(count) + '\t' + chunk.get_phrase()
                to_word = str(count) + '\t' + sentence_chunk_list[int(chunk.dst)].get_phrase()
                graph.add_edge(from_word, to_word)
    graph.layout()
    graph.draw('data/44_result.png')


if __name__ == '__main__':
    text_chunk_list = make_text_chunk()
    draw_graph(text_chunk_list)
