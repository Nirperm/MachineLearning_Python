"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，
文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
ただし，置換するときは，「代表参照表現（参照表現）」のように，
元の参照表現が分かるように配慮せよ
"""

import xml.etree.ElementTree as ET
# refer to dcoref info http://nlp.stanford.edu/software/corenlp_xml_description.shtml

if __name__ == '__main__':
    tree = ET.parse('data/nlp.xml')
    root = tree.getroot()

    sentences = root.findall('.//sentence')
    sentence_list = []  # size is 164
    for sentence in sentences:
        sentence_list.append(' '.join(map(lambda x: x.text, sentence.findall('.//word'))))

    """ All coreference size is 114 """
    mention_sentences = root.findall('.//mention//sentence')
    m_s_ids = [int(m_s_id.text) for m_s_id in mention_sentences]

    starts = root.findall('.//start')
    start_indexies = [int(start.text) for start in starts]

    ends = root.findall('.//end')
    end_indexies = [int(end.text) for end in ends]

    heads = root.findall('.//head')
    head_indexies = [int(head.text) for head in heads]

    nested_list = [sentence.split() for sentence in sentence_list]

    # FIXME i can not understand(pending)
    for m_s_id, start, end, head in zip(m_s_ids, start_indexies, end_indexies, head_indexies):
        print(sentence_list[m_s_id - 1][start:end].strip(), '\t', nested_list[m_s_id - 1][head - 1])
