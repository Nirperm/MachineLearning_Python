"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

import re
from section_20 import load_json
from section_20 import extract_uk_context

pattern = r'=+.+=+\n'
uk_context = extract_uk_context(load_json())

category_list = re.findall(pattern, uk_context)
section_dict = {}
for section in category_list:
    section = section.replace('\n', '')
    section_dict[section] = section.count('=')

for k, v in section_dict.items():
    if v is 4:
        section_dict[k] = 1
    elif v is 6:
        section_dict[k] = 2
    else:
        section_dict[k] = 3


for k, v in section_dict.items():
    print(k, v)
