import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from time import sleep

# Método de euler
def euler(f, y0, h, x):
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    for i in range(0, n-1):
        y[i+1] = y[i] + h * f(x[i], y[i])
    label = 'euler'
    return y, label
    
# Método de euler modificado
def euler_modificado(f, y0, h, x):
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    for i in range(0, n-1):
        y[i+1] = y[i] + h * f( x[i] + (0.5*h), y[i] + ((0.5*h) * f(x[i],y[i]) ) )
    label = "euler_modificado"
    return y, label
    
# Método de euler melhorado
def euler_melhorado(f, y0, h, x):
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    for i in range(0, n-1):
        y[i+1] = y[i] + (h*0.5) * f(x[i],y[i]) + (0.5*h)*f(x[i] + h, y[i] + h*f(x[i], y[i]))
    label = 'euler_melhorado'
    return y, label

# Método RK3
def RK3(f, y0, h, x):
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    for i in range(0, n-1):
        k1 = f(x[i], y[i])
        k2 = f( x[i] + (0.5*h), y[i] + (0.5*h)*k1 )
        k3 = f( x[i] + h, y[i] - h*k1 + 2*h*k2 )
        y[i+1] = y[i] + ( (1.0/6.0)*h*(k1 + 4*k2 + k3) )
        
    label = 'RK3'
    return y, label

# Método RK4
def RK4(f, y0, h, x):
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    for i in range(0, n-1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + (0.5*h), y[i] + (0.5*h)*k1)
        k3 = f(x[i] + (0.5*h), y[i] + (0.5*h)*k2)
        k4 = f(x[i] + h, y[i] + h*k3)
        y[i+1] = y[i] + ( (1.0/6.0) * h * (k1 + 2*k2 + 2*k3 + k4) )
        
    label = 'RK4'
    return y, label

# Método de Adams-Moulton
def Adams_Moulton(f, y0, h, x):
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    for i in range(0,n-1):
        y[i+2] = y[i+1] + (h/12) * (-f(x[i],y[i]) + 8*f(x[i+1], y[i+1]) + 5*f(x[i+2], y[i+2]) )
    
    label = 'Adams_Moulton' 
    return y, label

# Método de Adams-Bashforth
def Adams_Bashforth(f, y0, h, x):
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    for i in range(0, n-1):
        y[i+2] = y[i+1] + (h/2) * (-f(x[i],y[i]) + 3*f(x[i+1], y[i+1]))
    
    label = 'Adams_Bashforth' 
    return y, label


# Esse é o Main.
if __name__ == "__main__":
    # Dados de inicialização.

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

    y_numeric, label1  = RK4(f, y0, h, x) # Aqui eu chamo a função RK4 feita a cima ela retorna um vetor com os valores resultantes (y_numeric). label1 é uma variável que guarda o nome pra colocar no gráfico.
                                          # Voce pode substituir por outros metodos como euler, euler_melhorada, e outros. 
                                          # O mesmo acontece com o de baixo.
    y_numeric1, label2  = RK3(f, y0, h, x)# Aqui o mesmo que o de cima, Só que RK3.

    # Plot
    plt.plot(x, y_numeric, 'r',label=label1)      # Aqui plota o RK4.
    plt.plot(x, y_numeric1, '--b', label=label2)  # Aqui plota o RK3.


    plt.title("Gráfico") # O titulo do gráfico.
    plt.legend()         # Aqui ativa a legenda.

    plt.xlabel("X")      # Nome do Eixo X.
    plt.ylabel("Y")      # Nome do Eixo Y.
    plt.grid()           # Os quadradinhos que Aparecem no Gráfico.
    plt.rcParams['figure.figsize'] = (19,12) # Ajustar o tamanho do Gráfico.
    plt.show() # Mostrar o Gráfico na Tela.
