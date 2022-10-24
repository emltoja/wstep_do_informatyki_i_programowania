# Zadanie 3 Lista 5

# Funkcja rekurencyjna zwracająca podaną ilość pierwszych wyrazów ciągu Fibbonaciego 
def recurrent_fib(length):
    
    # Zwrócenie błędu w przypadku podania nieprawidłowego parametru
    if length <= 0:
        return 'Podano nieprawidłowy parametr'

    # Przypadki bazowe   
    if length == 1:
        return [0]
    if length == 2:
        return [0, 1]
    
    # Odwołanie do poprzedniej listy
    last_list = recurrent_fib(length - 1)
    # Obliczenie n-tego wyrazu ciągu fibbonaciego
    new_term = last_list[-1] + last_list[-2]
    
    return last_list + [new_term]


if __name__ == '__main__':
    print(recurrent_fib(700))

