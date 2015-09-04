"""
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

import pygraphviz as pgv


def draw_graph(xml_name):
    tag_collapsed = '<dependencies type=\"collapsed-dependencies\">'
    tag_collapsed_end = '</dependencies>'
    tag_governor = '</governor>'
    tag_dependent = '</dependent>'
    sentence_id = 0
    sentence_num = ''
    collapsed_flag = False

    graph = pgv.AGraph(strict=True, directed=True)
    for line in open(xml_name):
        if tag_collapsed in line:
            sentence_id += 1
            sentence_num = str(sentence_id) + '\t'
            collapsed_flag = True
        elif tag_collapsed_end in line:
            collapsed_flag = False
        elif collapsed_flag and tag_governor in line:
            governor = sentence_num + line.replace(tag_governor, '').split('>')[1]
        elif collapsed_flag and tag_dependent in line:
            dependent = sentence_num + line.replace(tag_dependent, '').split('>')[1]
            graph.add_edge(dependent, governor)
    graph.layout()
    graph.draw('data/57_result.png')


if __name__ == '__main__':
    xml_name = 'data/nlp.xml'
    draw_graph(xml_name)
