# Zadanie 6     Lista 2

def compare(string1, string2):

    string1 = string1.upper()
    string2 = string2.upper()

    result = []
    length = min(len(string1), len(string2))

    for i in range(length):
        result.append(string1[i] == string2[i])

    result += [False] * abs(len(string1) - len(string2))
    return result

print(compare('oho', 'oho'))
