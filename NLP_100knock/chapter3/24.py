"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""

import re
from section_20 import load_json
from section_20 import extract_uk_context


pattern = r'((File|ファイル|=):?.+\.(png|PNG|jpeg|jpg|svg))'
uk_context = extract_uk_context(load_json())

match_media = re.finditer(pattern, uk_context)

media_list = []
for m in match_media:
    media_list.append(m.group(0))

trim_media_list = ''.join(media_list).replace('=', '@') \
                                     .replace('[[ファイル:', '@') \
                                     .replace('ファイル:', '@') \
                                     .replace('File:', '@') \
                                     .split('@')  # '@'をsplitの目印にしている
del trim_media_list[0]  # split('@')の影響で先頭は空白が入るので

for media_file in trim_media_list:
    if len(media_file) is 1:  # 空白が入ってる場合
        pass
    else:
        print(media_file.strip())
