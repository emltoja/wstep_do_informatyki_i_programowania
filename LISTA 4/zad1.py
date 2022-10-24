# Zadanie 1 Lista 4
import matplotlib.pyplot as plt
import numpy as np

# Funkcja tworząca wykres i wyświetlająca go
def visualize():
    
    # Utworzenie osi x i y z odpowiednimi wartościami
    xaxis = np.linspace(1, 50)
    yaxis = xaxis/100*100 - xaxis
    
    plt.scatter(xaxis, yaxis)
    plt.title("Błędy w reprezentacji liczb zmiennoprzecinkowych", pad=20)
    plt.xlabel('N')
    plt.ylabel('N/100*100 - N')
    plt.show()
    

visualize()
    
    

