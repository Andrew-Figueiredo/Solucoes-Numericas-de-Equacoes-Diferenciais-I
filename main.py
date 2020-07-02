import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from time import sleep

# def analytic(f, y0, x):
#    return odeint(f, y0, x)

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
    n=len(x)
    y=np.zeros(n)
    y[0]=y0
    for i in range(0, n-1):
        k1 = f(x[i], y[i])
        k2 = f( x[i] + (0.5*h), y[i] + (0.5*h) * k1 )
        k3 = f( x[i] + h, y[i] - h*k1 + 2*h*k2 )
        y[i+1] = y[i] + (1.0/6.0)*(k1 + 4*k2 + k3)
        
    label = 'RK3'
    return y, label

# Método RK4
def RK4(f, y0, h, x):
    n=len(x)
    y=np.zeros(n)
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
    y=np.zeros(n)
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


if __name__ == "__main__":
   
    # Dados de inicialização

    # Função
    def f(x,y):
        return y

        
    x0 = 0
    x = 5
    y0= 1
    h = 0.1


    n = (int)((x - x0)/h)
    x = np.arange(x0,x+h,h)

    # Métodos
    # y_analytic = odeint(f, y0, x)

    y_numeric, label1  = RK4(f, y0, h, x) 
    y_numeric1, label2  = euler(f, y0, h, x) 

    # Plot

#    plt.plot(x, y_analytic, '*r')
    plt.plot(x, y_numeric, 'r',label=label1)
    plt.plot(x, y_numeric1, '--b', label=label2)


    plt.title("Gráfico")
    plt.legend()

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.rcParams['figure.figsize'] = (19,12)
    plt.show()
