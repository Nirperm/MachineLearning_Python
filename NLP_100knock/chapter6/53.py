"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""

# import corenlp
from corenlp import batch_parse
from section_50 import divide_content
import xmltodict


if __name__ == '__main__':
    corenlp_dir = '/usr/local/lib/stanford-corenlp-full-2013-06-20/'
    raw_text_directory = 'data/'
    parsed = batch_parse(raw_text_directory, corenlp_dir, raw_output=True)
    print(parsed)
    # result = xmltodict.parse(parsed)
    # print(result)
    """
    parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)
    sentence_list = divide_content()
    for word in sentence_list:
        print(parser.parse(word))
    # contents = ''.join(sentence_list)
    # result_json = json.loads(parser.parse(contents))
    # print(result_json)
    """
