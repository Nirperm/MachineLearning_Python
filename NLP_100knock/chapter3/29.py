"""
国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

import re
import urllib
from section_20 import load_json
from section_20 import extract_uk_context


pattern = r'\|(.+ )= (.+)'
uk_context = extract_uk_context(load_json())

template_dict = {}
template_list = re.findall(pattern, uk_context)

ref_pattern = re.compile('<ref.+')

for template_tuple in template_list:
    value = template_tuple[1].replace('\'', '') \
                             .replace('[', '') \
                             .replace(']', '') \
                             .replace('<br/>', '') \
                             .replace('<br />', '') \
                             .replace('{', '') \
                             .replace('}', '') \
                             .replace('|', ' ') \
                             .replace('<ref>', ' ') \
                             .replace('</ref>', ' ')
    trim_value = ref_pattern.sub('', value)
    template_dict[template_tuple[0].strip()] = trim_value

flag_image = template_dict['国旗画像']
url = 'https://en.wikipedia.org/w/api.php'
params = '?query&titles=Image:{0}&prop=imageinfo'.format(flag_image)

