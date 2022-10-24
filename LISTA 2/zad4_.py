# Zadanie 4     Lista 2

def char_counter(string, char):
    string = string.upper()
    char = char.upper()
    count = 0
    for letter in string:
        if char == letter:
            count += 1
    return count

string = input('Podaj słowo ')
char = input('Podaj literę ')

print(char_counter(string, char))
