# Zadanie 3, 4 Lista 3

letters = 'abcdefghijklmnopqrstuvwxyz'

text = '''
"N zna, n cyna, n pnany: Cnanzn!"
N PBQR BS RGUVPNY ORUNIVBE SBE CNGVRAGF:
1. QB ABG RKCRPG LBHE QBPGBE GB FUNER LBHE QVFPBZSBEG. Vaibyirzrag
jvgu gur cngvrag’f fhssrevat zvtug pnhfr uvz gb ybfr inyhnoyr
fpvragvsvp bowrpgvivgl.
2. OR PURRESHY NG NYY GVZRF. Lbhe qbpgbe yrnqf n ohfl naq gelvat
yvsr naq erdhverf nyy gur tragyrarff naq ernffhenapr ur pna trg
.
3. GEL GB FHSSRE SEBZ GUR QVFRNFR SBE JUVPU LBH NER ORVAT GERNGRQ.
Erzrzore gung lbhe qbpgbe unf n cebsrffvbany erchgngvba gb
hcubyq
'''

# Funkcja szyfrująca dany tekst algorytmem rot13
def rot13(text):

    text = text.lower()
    result = ''

    for letter in text:

        if letter in letters:
            index = letters.index(letter)
            result += letters[(index + 13) % 26]
        else:
            result += letter

    return result

print(rot13(text))
