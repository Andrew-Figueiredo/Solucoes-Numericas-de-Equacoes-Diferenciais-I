import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class atividade:
    def __init__(self, f, y_init, x_init, x_end, h ):
        self.f = f
        self.x = np.arange(x_init,x_end+h,h)
        self.y = np.zeros(len(self.x))
        self.y[0] = y_init
        self.h = h
        self.n = len(self.x)-1
        self.label = []
        self.y_analytic = []

    def euler(self):
        for i in range(0, self.n):
            self.y[i+1] = self.y[i] + (self.h * self.f(self.x[i], self.y[i]) )
        label = 'euler'
        self.addGraph(self.y, label, '^b')    

    def Adams_Bashforth_Moulton_4_ordem(self ):
        
        j = 0
        while j<3:
            self.RK4(j)
            j+=1

        j = 3
        while j < self.n :
            #preditor
            yp = self.y[j] + (self.h/24)*(55*self.f(self.x[j],self.y[j]) - 59*self.f(self.x[j-1], self.y[j-1]) + 37*self.f(self.x[j-2], self.y[j-2]) - 9*self.f(self.x[j-3], self.y[j-3]))
            # corretor
            yc = self.y[j] + (self.h/24)*(9*self.f(self.x[j+1],yp) + 19*self.f(self.x[j],self.y[j]) - 5*self.f(self.x[j-1],self.y[j-1]) + self.f(self.x[j-2],self.y[j-2]))

            self.y[j+1] = self.y[j] + (self.h/24)*(9*self.f(self.x[j+1],yc) + 19*self.f(self.x[j],self.y[j]) - 5*self.f(self.x[j-1],self.y[j-1]) + self.f(self.x[j-2],self.y[j-2]))
            
            j+=1

        label = 'Adams_Bashforth_Moulton_4_ordem'
        self.addGraph(self.y, label, '-g')

    def Dormand_Price_4_ordem(self):
        for i in range(0,self.n):
            k1 = self.h * self.f(self.x[i], self.y[i])
            k2 = self.h * self.f(self.x[i] + ((1.0/5.0)*self.h), self.y[i] + ((1.0/5.0)*k1))
            k3 = self.h * self.f(self.x[i] + ((3.0/10.0)*self.h), self.y[i] + ((3.0/40.0)*k1) + ((9.0/40.0)*k2))
            k4 = self.h * self.f(self.x[i] + ((4.0/5.0)*self.h), self.y[i] + ((44.0/45.0)*k1) - ((56.0/15.0)*k2) + ((32.0/9.0)*k3))
            k5 = self.h * self.f(self.x[i] + ((8.0/9.0)*self.h), self.y[i] + ((19372.0/6561.0)*k1) - ((25360.0/2187.0)*k2) + ((64448.0/6561.0)*k3) - ((212.0/729.0)+k4))
            k6 = self.h * self.f(self.x[i] + self.h, self.y[i] + ((9017.0/3168.0)*k1) - ((355.0/33.0)*k2) - ((46732.0/5247.0)*k3) + ((49.0/176.0)*k4) - ((5103.0/18656.0)*k5))
            k7 = self.h * self.f(self.x[i] + self.h, self.y[i] + ((35.0/384.0)*k1) + ((500.0/1113.0)*k3) + ((125.0/192.0)*k4) - ((2187.0/6784.0)*k5) + ((11.0/84.0)*k6))

            self.y[i+1] = self.y[i] + ((35.0/384.0)*k1) + ((500.0/1113.0)*k3) + ((125.0/192.0)*k4) - ((2187.0/6784.0)*k5) + ((11.0/84.0)*k6) 

        label = 'Dormand_Price_4_ordem'
        self.addGraph(self.y, label, '--b')

    def analytic(self):
        self.y_analytic = odeint(self.f, self.y[0], self.x)
        label = 'Analítica'
        self.addGraph(self.y, label, '*r')
    
    def getX(self):
        return self.x

    def RK4(self, i):
        k1 = self.f(self.x[i], self.y[i])
        k2 = self.f(self.x[i] + (0.5*self.h), self.y[i] + (0.5*self.h)*k1)
        k3 = self.f(self.x[i] + (0.5*self.h), self.y[i] + (0.5*self.h)*k2)
        k4 = self.f(self.x[i] + self.h, self.y[i] + self.h*k3)
        self.y[i+1] = self.y[i] + ( (1.0/6.0) * self.h * (k1 + 2*k2 + 2*k3 + k4) )

    def addLabel(self, label):
        self.label.append(label)

    def addGraph(self, y, label, cor):
        x = self.getX()
        plt.plot(x, y, cor, label = label )

    def viewGraph(self, namefig):
        plt.rcParams['figure.figsize'] = (10,7)  
        plt.title(str(namefig)) 
        plt.legend()         

        plt.xlabel("X")         
        plt.ylabel("Y")        
        plt.grid()  
        plt.savefig('Atividade/result/' + str(namefig))         
        plt.show()
        

    def valorY(self):
        print("Resultado Numérico: ")
        print(self.y)
        print("Resultado Analítico: ")
        print(self.y_analytic)


