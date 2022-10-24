# Zadanie 6 Lista 5
from string import ascii_lowercase, ascii_uppercase

letters = ''

for uppercase, lowercase in zip(ascii_uppercase, ascii_lowercase):
    letters += uppercase
    letters += lowercase
    

def check_type(lst):

    for element in lst:
        if isinstance(element, str):
            return str
    return int

def is_sorted(lst):

    def int_list():

        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True
    
    def string_list():

        for i in range(len(lst) - 1):
            if letters.index(lst[i]) > letters.index(lst[i + 1]):
                return False
        return True

    if check_type(lst) == str:
        return string_list()
    if check_type(lst) == int:
        return int_list()


print(is_sorted('AaBbDc'))
