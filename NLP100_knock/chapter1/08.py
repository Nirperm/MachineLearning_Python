"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(string):
    encrypted_list = [ord(x) for x in string]
    encrypted_str_list = [str(x) for x in encrypted_list]
    print('encrypted is ', ''.join(encrypted_str_list))
    decrypted_list = [chr(x) for x in encrypted_list]
    decrypted = ''.join(decrypted_list)
    print('decrypted is ', decrypted)
    print('decoding result is ', string == decrypted)

string = "a1s2d3f4g5h6j7k8l9"
cipher(string)
