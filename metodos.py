import numpy as np
from scipy.integrate import odeint

class Metodos:

    def analytic(self, f, y_init, h, x):
        y = odeint(f, y_init[0], x)
        label = "Analitico"
        return y, label

    # Método de euler
    def euler(self, f, y_init, h, x):
        n = len(x)
        y = np.zeros(n)
        y[0] = y_init[0]
        for i in range(0, n-1):
            y[i+1] = y[i] + h * f(x[i], y[i])
        label = 'euler'
        return y, label
        
    # Método de euler modificado
    def euler_modificado(self, f, y_init, h, x):
        n = len(x)
        y = np.zeros(n)
        y[0] = y_init[0]
        for i in range(0, n-1):
            y[i+1] = y[i] + h * f( x[i] + (0.5*h), y[i] + ((0.5*h) * f(x[i],y[i]) ) )
        label = "euler_modificado"
        return y, label
        
    # Método de euler melhorado
    def euler_melhorado(self, f, y_init, h, x):
        n = len(x)
        y = np.zeros(n)
        y[0] = y_init[0]
        for i in range(0, n-1):
            y[i+1] = y[i] + (h*0.5) * f(x[i],y[i]) + (0.5*h)*f(x[i] + h, y[i] + h*f(x[i], y[i]))
        label = 'euler_melhorado'
        return y, label

    # Método RK3
    def RK3(self, f, y_init, h, x):
        n = len(x)
        y = np.zeros(n)
        y[0] = y_init[0]
        for i in range(0, n-1):
            k1 = f(x[i], y[i])
            k2 = f( x[i] + (0.5*h), y[i] + (0.5*h)*k1 )
            k3 = f( x[i] + h, y[i] - h*k1 + 2*h*k2 )
            y[i+1] = y[i] + ( (1.0/6.0)*h*(k1 + 4*k2 + k3) )
            
        label = 'RK3'
        return y, label

    # Método RK4
    def RK4(self, f, y_init, h, x):
        n = len(x)
        y = np.zeros(n)
        y[0] = y_init[0]
        for i in range(0, n-1):
            k1 = f(x[i], y[i])
            k2 = f(x[i] + (0.5*h), y[i] + (0.5*h)*k1)
            k3 = f(x[i] + (0.5*h), y[i] + (0.5*h)*k2)
            k4 = f(x[i] + h, y[i] + h*k3)
            y[i+1] = y[i] + ( (1.0/6.0) * h * (k1 + 2*k2 + 2*k3 + k4) )
            
        label = 'RK4'
        return y, label

    # Método de Adams-Moulton
    def Adams_Moulton(self, f, y_init, h, x):
        n = len(x)
        y = np.zeros(n)
        y[0] = y_init[0]
        y[1] = y_init[1]
        for i in range(0, n-1):
            y[i+2] = y[i+1] + (h/12) * (-f(x[i],y[i]) + 8*f(x[i+1], y[i+1]) + 5*f(x[i+2], y[i+2]) )
        
        label = 'Adams_Moulton' 
        return y, label

    # Método de Adams-Bashforth
    def Adams_Bashforth(self, f, y_init, h, x):
        n = len(x)
        y = np.zeros(n)
        y[0] = y_init[0]
        y[1] = y_init[1]
        for i in range(0, n-1):
            y[i+2] = y[i+1] + (h/2) * (-f(x[i],y[i]) + 3*f(x[i+1], y[i+1]))
        
        label = 'Adams_Bashforth' 
        return y, label

