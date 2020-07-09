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
        return y

    # Inicialização
    x0 = 0 # X Inicial
    x = 5 # X Final
    y0= 1 # Y inicial
    h = 0.1 # Passo

    n = (int)((x - x0)/h) # Tamanho de intervalos
    x = np.arange(x0,x+h,h) # Criação do intervalo X

    y_numeric, label1  = metodo.RK4(f, y0, h, x) # Aqui eu chamo a função RK4 feita a cima ela retorna um vetor com os valores resultantes (y_numeric). label1 é uma variável que guarda o nome pra colocar no gráfico.
                                          # Voce pode substituir por outros metodos como euler, euler_melhorada, e outros. 
                                          # O mesmo acontece com o de baixo.
    y_numeric1, label2  = metodo.RK3(f, y0, h, x)# Aqui o mesmo que o de cima, Só que RK3.
    y_analytic, label3  = metodo.RK4(f, y0, h, x)

    # Plot
    plt.plot(x, y_numeric, 'r',label=label1)      # Aqui plota o RK4.
    plt.plot(x, y_numeric1, '--b', label=label2)  # Aqui plota o RK3.
    plt.plot(x, y_analytic, '*g', label=label3)   # Aqui plota o analitico.


    plt.title("Gráfico") # O titulo do gráfico.
    plt.legend()         # Aqui ativa a legenda.

    plt.xlabel("X")      # Nome do Eixo X.
    plt.ylabel("Y")      # Nome do Eixo Y.
    plt.grid()           # Os quadradinhos que Aparecem no Gráfico.
    plt.rcParams['figure.figsize'] = (19,12) # Ajustar o tamanho do Gráfico.
    plt.show() # Mostrar o Gráfico na Tela.
