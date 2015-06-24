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
template_list = re.findall(pattern, uk_context)
join_list = []
for template in template_list:
    join_list.append(template[0] + template[1].replace('\'', ''))
    # template_dict[template[0]] = template[1].replace('\'', '')

print(''.join(join_list))
"""
for k, v in template_dict.items():
    print(k, v)
"""
