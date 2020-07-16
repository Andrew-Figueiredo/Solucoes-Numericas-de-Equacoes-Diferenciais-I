from Atividades import atividade
import numpy as np
from time import sleep

if __name__ == "__main__":
    try: 
        while(True):   
            select = input("Digite qual o PVI você quer testar(a,b,c, 0 pra sair): ")

            if select == "a":
                # 12.2 - A
                # Função
                f = lambda x,y: (y**2) + 1
            
                # Inicialização
                x0 = 0 # X Inicial
                x  = 1 # X Final
                y0 = 0 # Y inicial
                h  = 0.2 # Passo

                atividade_A = atividade(f, y0, x0, x, h )
                # Resolvendo Adams_Bashforth_Moulton_4_ordem
                atividade_A.Adams_Bashforth_Moulton_4_ordem()
                # Resolvendo de forma analitica utilizando odeint
                atividade_A.analytic()
                # Mostrar o valor de Y e analytic
                atividade_A.valorY()
                
                # Plotar gráfico
                atividade_A.viewGraph()
            elif select == "b":
            
                # 12.2 - B
                f = lambda x,y: -2*x*y
            
                # Inicialização
                x0 = 0 # X Inicial
                x  = 0.6 # X Final
                y0 = 1 # Y inicial
                h  = 0.1 # Passo

                atividade_B = atividade(f, y0, x0, x, h )
                # Resolvendo Adams_Bashforth_Moulton_4_ordem
                atividade_B.Adams_Bashforth_Moulton_4_ordem()
                # Resolvendo de forma analitica utilizando odeint
                atividade_B.analytic()
                # Mostrar o valor de Y e analytic
                atividade_B.valorY()
                
                # Plotar gráfico
                atividade_B.viewGraph()

            elif select == "c":
                # 12.2 - C
                f = lambda x,y: -x*y
            
                # Inicialização
                x0 = 0 # X Inicial
                x  = 0.3 # X Final
                y0 = 2 # Y inicial
                h  = 0.1 # Passo

                atividade_C = atividade(f, y0, x0, x, h )
                # Resolvendo Adams_Bashforth_Moulton_4_ordem
                atividade_C.Adams_Bashforth_Moulton_4_ordem()
                # Resolvendo de forma analitica utilizando odeint
                atividade_C.analytic()
                # Mostrar o valor de Y e analytic
                atividade_C.valorY()
                
                # Plotar gráfico
                atividade_C.viewGraph()
            
            elif select == "0":
                print("Saindo . . .")
                sleep(2)
                exit()
            else:
                print("Nenhuma opção selecionada!")
    except Exception as e:
        print(e)    