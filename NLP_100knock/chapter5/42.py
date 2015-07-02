"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""

from section_40 import Morph
from section_41 import Chunk

cabocha_list = Morph.read_cabocha()
teos_list = Chunk.read_cabocha()

chunk = Chunk(cabocha_list[0], teos_list[0], teos_list[1])

surface_list = []
dst_list = []

for dst in chunk.dst:
    dst_list.append(dst)

for line_list in chunk.morphs:
    if len(line_list) > 1 and line_list[1] != '記号':
        surface_list.append(line_list[0])


print(','.join(dst_list).replace(',', '\t'))
print(','.join(surface_list).replace(',', '\t'))
