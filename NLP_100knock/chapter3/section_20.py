"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""


import json


def load_json():
    input_file = 'data/jawiki-country.json'
    data_list = []

    with open(input_file) as f:
        for line in f:
            data_list.append(json.loads(line))
        return data_list


def extract_uk_context(data_list):
    for topic in data_list:
        if topic['title'] == 'イギリス':
            uk_context = topic['text']
            return uk_context

if __name__ == '__main__':
    data_list = load_json()
    uk_context = extract_uk_context(data_list)
    print(uk_context)
