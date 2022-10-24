# Zadanie 4 Lista 4

import numpy as np

a = c = 1
# Przedział wartości b
segment = np.linspace(10**7.4, 10**8.5, 100)

# Funkcja zwracająca pierwiastki liczone obiema metodami
def get_roots(a, b, c):
    
    delta = b**2 - 4*a*c
    
    # Funkcja licząca pierwiastki pierwszą metodą
    def first_method():
    
        x2 = 1/(2*a) * (-b + np.sign(b) * np.sqrt(delta))
        x1 = 1/(2*a) * (-b - np.sign(b) * np.sqrt(delta))
        
        return x1, x2

    # Funkcja licząca pierwiastki drugą metodą
    def second_method():
        
        x1 = 1/(2*a) * (-b - np.sign(b) * np.sqrt(delta))
        x2 = c / (a * x1)
        
        return x1, x2
    
    return first_method(), second_method()

# Funkcja wypisująca pierwiastki dla poszczególnych wartości b
def print_result():
    
    for b in segment:
        print(get_roots(a, b, c))

print_result()