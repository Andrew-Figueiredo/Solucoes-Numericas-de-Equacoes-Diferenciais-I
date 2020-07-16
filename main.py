import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from time import sleep
from metodos import Metodos


# Esse é o Main.
if __name__ == "__main__":
    # Dados de inicialização.
    metodo = Metodos()
    # Essa é a função que aparece quando isolamos o y'
    def f(x,y):
        return y**2 + 1

    # Inicialização
    x0 = 0 # X Inicial
    x = 1 # X Final
    y0= 0 # Y inicial
    h = 0. # Passo

    n = (int)((x - x0)/h) # Tamanho de intervalos
    x = np.arange(x0,x+h,h) # Criação do intervalo X

    y_numeric, label1  = metodo.analytic(f, y0, h, x) 
    y_numeric1, label2  = metodo.euler(f, y0, h, x)
    #y_analytic, label3  = metodo.RK4(f, y0, h, x)

    # Plot
    plt.plot(x, y_numeric, 'r',label=label1)      
    plt.plot(x, y_numeric1, '--b', label=label2)  
   # plt.plot(x, y_analytic, '*g', label=label3)   


    plt.title("Gráfico") 
    plt.legend()         

    plt.xlabel("X")         
    plt.ylabel("Y")        
    plt.grid()           
    plt.rcParams['figure.figsize'] = (19,12)  
    plt.show() 
