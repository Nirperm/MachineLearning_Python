"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

import re
from section_20 import load_json
from section_20 import extract_uk_context

pattern = r'=+.+=+\n'
uk_context = extract_uk_context(load_json())

category_list = re.findall(pattern, uk_context)
category_lines = ','.join(category_list).replace('\n', '')
print(category_lines)
