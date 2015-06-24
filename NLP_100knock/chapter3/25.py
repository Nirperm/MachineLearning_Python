"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．
"""

import re
from section_20 import load_json
from section_20 import extract_uk_context


pattern = r'\|(.+ )= (.+)'
uk_context = extract_uk_context(load_json())


template_dict = {}
template_list = re.findall(pattern, uk_context)
for template in template_list:
    template_dict[template[0]] = template[1]

for k, v in template_dict.items():
    print(k, v)
