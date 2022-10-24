# Zadanie 7 Lista 5

# Importy
from zad5 import delete_invalid_chars

# Funkcja sprawdzająca czy dwa słowa są anagramami
def check(string1, string2):

    # Usunięcie niepotrzebnych znaków
    string1 = delete_invalid_chars(string1).lower()
    string2 = delete_invalid_chars(string2).lower()

    if len(string1) != len(string2):
        return False
    
    for letter in string1:
        if string1.count(letter) != string2.count(letter):
            return False
    
    return True

print(check('bark', 'krab'))



