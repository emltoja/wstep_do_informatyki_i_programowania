# Zadanie 4 Lista 5

# Importy
from zad3 import recurrent_fib
from time import time

def iterative_fib(length):

    # Zwrócenie błędu w przypadku gdy podano nieprawidłowy parametr
    if length <= 0:
        return 'Podano nieprawidłowy parametr'
    
    # Przypadki bazowe
    if length == 1:
        return [0]
    if length == 2:
        return [0, 1]

    result = [0, 1]

    for i in range(length - 2):
        result.append(result[-1] + result[-2])
    
    return result

# Funkcja mierząca czas wykonania funkcji iteracyjnej oraz rekurencyjnej
def mesaure_time(num_of_iterations):

    start1 = time()
    for i in range(num_of_iterations):
        iterative_fib(100)
    stop1 = time()

    start2 = time()
    for i in range(num_of_iterations):
        recurrent_fib(100)
    stop2 = time()

    return 'Czas wykonania funkcji iteracyjnej: ' + str((stop1 - start1) / num_of_iterations) + '\n' + \
           'Czas wykonania funkcji rekurencyjnej: ' + str((stop2 - start2) / num_of_iterations)


print(mesaure_time(10000))