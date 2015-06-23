"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import re
from section_20 import load_json
from section_20 import extract_uk_context

pattern = r'=+([^=]+)=+\n'
uk_context = extract_uk_context(load_json())

category_list = re.findall(pattern, uk_context)
categories = ','.join(category_list)
print(categories)
