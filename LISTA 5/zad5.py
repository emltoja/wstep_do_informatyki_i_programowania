# Zadanie 5 Lista 5

from string import ascii_letters

def delete_invalid_chars(string):
    
    valid_symbols = [letter for letter in string if letter in ascii_letters]
    result = ''
    for letter in valid_symbols:
        result += letter
    return result

def is_palindrome(string):

    valid_string = delete_invalid_chars(string)

    return valid_string == valid_string[::-1]

if __name__ == '__main__':
    print(is_palindrome('a man a plan a canal: panama!'))


