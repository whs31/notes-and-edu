# -- task 5 --
"""
Define a function named `cipher`
Function must be able to decode ciphers:
    - Atbash
    - Caesar
    - Vigenere
Input of fn:
    - initial text (T: str)
    - encryption key named `key`, default="", (T: str)
        - Atbash has no key
        - Caesar can have either "n to the left" or "n to the right" where n = any number (int)
        - Vigenere can have any str in letters as a key
    - encoding mode (name this parameter as encode, set the default value as True (T: bool))
        - encode=True means encode the initial text
        - encode=False means decode the initial text
    - cipher type (a named argument in the format `type=True`)
Output:
    - an uppercase string with encoded/decoded initial text

TEST CASES:
1.
INPUT: cipher('Paper Jam Dipper says: «AUUGHWXQHGADSADUH!»', atbash=True)
OUTPUT: "KZKVI QZN WRKKVI HZBH: «ZFFTSDCJSTZWHZWFS!»"

2.
INPUT: cipher('ZHOFRPH WR JUDYLWB IDOOV.', '3 to the right', encode=False, caesar=True)
OUTPUT: "WELCOME TO GRAVITY FALLS."

3.
INPUT: cipher('pvrek big qf. jcdqzrf’ znvefh obcx: «c bewrs vvutbfl bt bknx cvay bknx cvay bknx»', 'noncanon', encode=False, vigenere=True)
OUTPUT: "CHECK OUT DR.WADDLES’ LATEST BOOK: «A BRIEF HISTORY OF OINK OINK OINK OINK»"
"""


def cipher(text: str,
           key: str = "",
           encode: bool = True,
           atbash: bool = False,
           caesar: bool = False,
           vigenere: bool = False):
    if atbash:
        translator = {k: v for k, v in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ZYXWVUTSRQPONMLKJIHGFEDCBA")}
        if encode:
            plain_text = text.upper()
            j = []
            for c in plain_text:
                if c.isalpha(): j.append(translator[c])
                else: j.append(c)
            if j[-1] == ' ': j.pop()
            return ''.join(j)
        else:
            plain = [translator[c] if c.isalpha() else c for c in text]
            return ''.join(plain)
    if caesar:
        n = int(key.split()[0])
        right = key.split()[-1] == 'right'
        if encode:
            if right: return ''.join(chr((ord(c) - 65 + n) % 26 + 65) if c.isalpha() else c for c in text)
            else: return ''.join(chr((ord(c) - 65 - n) % 26 + 65) if c.isalpha() else c for c in text)
        else:
            if right: return ''.join(chr((ord(c) - 65 - n) % 26 + 65) if c.isalpha() else c for c in text)
            else: return ''.join(chr((ord(c) - 65 + n) % 26 + 65) if c.isalpha() else c for c in text)
    if vigenere:
        if encode:
            encrypted_text = ""
            key_length = len(key)

            for i in range(len(text)):
                char = text[i]
                if char.isalpha():
                    key_char = key[i % key_length]
                    shift = ord(key_char.lower()) - ord('a')
                    if char.isupper(): encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
                    else: encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
                else: encrypted_text += char
            return encrypted_text
        else:
            decrypted_text = ""
            key_length = len(key)

            no_spaces = [char for char in text if char.isalpha()]
            for i in range(len(no_spaces)):
                char = no_spaces[i]
                if char.isalpha():
                    key_char = key[i % key_length]
                    shift = ord(key_char.lower()) - ord('a')
                    if char.isupper(): decrypted_text += chr((ord(char) - shift - ord('A') + 26) % 26 + ord('A'))
                    else: decrypted_text += chr((ord(char) - shift - ord('a') + 26) % 26 + ord('a'))
                else: decrypted_text += char
            decrypted_text = decrypted_text.upper()
            for i in range(len(text)):
                if not text[i].isalpha():
                    decrypted_text = decrypted_text[:i] + text[i] + decrypted_text[i:]
            return decrypted_text.upper()

assert cipher('Paper Jam Dipper says: «AUUGHWXQHGADSADUH!»', atbash=True) == "KZKVI QZN WRKKVI HZBH: «ZFFTSDCJSTZWHZWFS!»"
assert cipher('ZHOFRPH WR JUDYLWB IDOOV.', '3 to the right', encode=False, caesar=True) == "WELCOME TO GRAVITY FALLS."
assert cipher('pvrek big qf. jcdqzrf’ znvefh obcx: «c bewrs vvutbfl bt bknx cvay bknx cvay bknx»', 'noncanon', encode=False, vigenere=True) == "CHECK OUT DR. WADDLES’ LATEST BOOK: «A BRIEF HISTORY OF OINK OINK OINK OINK OINK»"
