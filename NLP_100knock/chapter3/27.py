"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
（参考: マークアップ早見表）．
"""

import re
from section_20 import load_json
from section_20 import extract_uk_context


pattern = r'\|(.+ )= (.+)'
uk_context = extract_uk_context(load_json())

# template_dict = {}
join_list = []
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
    join_list.append(template_tuple[1] + trim_value)
    # template_dict[template_tuple[0]] = trim_value

print(''.join(join_list))
"""
for k, v in template_dict.items():
    print(k, v)
"""
