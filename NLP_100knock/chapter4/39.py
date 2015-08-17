"""
39. Zipfの法則 (右肩下がりの図)
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

import matplotlib
matplotlib.use('Agg')
import platform
import matplotlib.pyplot as plt
from section_30 import make_mecab_data

""" for Mac """
if platform.system() == 'Darwin':
    font_prop = matplotlib.font_manager.FontProperties(fname='/Library/Fonts/Osak.ttf')
else:
    font_prop = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")

mecab_dict_list = make_mecab_data()
word_count_dict = {}

for i, mecab_dict in enumerate(mecab_dict_list):
    if mecab_dict['surface'] not in word_count_dict:
        word_count_dict[mecab_dict['surface']] = 0
    word_count_dict[mecab_dict['surface']] += 1

order_word_count_list = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)

word_list = []
count_list = []

for ele in order_word_count_list[:10]:
    word_list.append(ele[0])
    count_list.append(ele[1])

bar_width = 200

"""
plt.bar(count_list, count_list, color='blue', width=bar_width, align='center')
plt.xticks(count_list, word_list, fontproperties=font_prop)
plt.savefig('data/37.png')
"""
