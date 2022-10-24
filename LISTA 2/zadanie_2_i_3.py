# Zadanie 2 i 3     Lista 2

def char_finder(string, char, start):
    if start < 1 or start > len(string):
        return 'Podano nieprawidłową pozycję startową'
    string = string.upper()
    char = char.upper()
    count = 1
    for letter in string[start-1:]:
        if letter == char:
            return count
        count += 1
    return 'Brak literki w słowie'

string = input('Podaj słowo ')
char = input('Podaj literke ')
start = int(input('Podaj pozycję startową '))

print(char_finder(string, char, start))
