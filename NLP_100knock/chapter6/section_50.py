"""
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし
，入力された文書を1行1文の形式で出力せよ．
"""
import re


def divide_content(content_list):
    result_list = []
    for line in content_list:
        if len(line) != 1:
            result_list.append(line.replace('(e.g,', '(e.g.').strip() + '\n')
    return result_list

if __name__ == '__main__':
    f = open('data/nlp.txt', encoding='utf-8')
    content = f.read()
    f.close()
    content = content.replace('(e.g.', '(e.g,')
    content_list = re.split(r"(\.|;|:|\?|!)\s", content)
    result_list = divide_content(content_list)
    for line in result_list:
        print(line)
