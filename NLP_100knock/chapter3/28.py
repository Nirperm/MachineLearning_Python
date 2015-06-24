"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""

import re
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
    template_dict[template_tuple[0]] = trim_value

for k, v in template_dict.items():
    print(k, v)
