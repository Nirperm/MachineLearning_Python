"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
police_car = '「パトカー」'
taxi = '「タクシー」'

word_list = []
for i in range(6):
        word_list.append(police_car[i])
        if taxi[i] != '「':
            if taxi[i] != '」':
                word_list.append(taxi[i])

print(' '.join(word_list))
