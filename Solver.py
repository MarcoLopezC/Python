# importar librerias
import math
#import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from tabulate import tabulate

# funcion
def f1(x):
    # funcion
    return math.exp(1) ** (-(x ** 2) + 2) - x * math.sin(2 * x - 3) + 1

# definimos la variable
a =  float(input('Cual es la variable a? '))
b =   float(input('Cual es la variable b? '))
xm = (a + b) / 2  # resultado
ep=0 #Error permitido
e=0  #cuando sale un error
limite = int(input('Cual es el limite ? '))     # se ingresa el limite de la variable
aa=a
bb=b
xmm=xm

#datos de la estructura

arreglo=([1, a ,b ,xm ,f1(a) ,f1(b) ,f1(xm) ,e ,ep ]) #arreglo
valores=([arreglo])  #lista del areglo objeto

#datos a imprimir

for n in range(0,limite-1):

    if valores[n][4]*valores[n][6] >= 0.0:
        aa = aa
        bb = (valores[n][3])
    else:
        aa=(valores[n][3])
        bb=bb
    xmm=(aa+bb)/2
    fa= f1(a)
    fb= f1(b)
    fxm= f1(xm)
    if n==0: #primer intento
        valores.append([n+2,aa,bb,xmm,fa,fb,fxm,xmm-xm])
    else:
        valores.append([n+2,aa,bb,xmm,fa,fb,fxm,xmm-xm])

    #imprime la tabla de valores

print(tabulate(valores,headers=['#','a','b','xm','f(a)','f(b)','f(xm)','Error','Errorp']))

   # configura os ejes del centro

     #x = np.linspace(-20,20,1000)
     #fig = plt.figure()
     #ax = fig.add_subplot(1, 1, 1)
     #ax.spines['left'].set_position('center')
     #ax.spines['bottom'].set_position('zero')
     #ax.spines['right'].set_position('none')
     #ax.spines['top'].set_position('none')
     #ax.xaxis.set_ticks_position('bottom')
     #ax.yaxis.set_ticks_position('left')

     #Trazar la funcion
     #plt.plot(x,[f1(i) for i in x])
     #plt.show()
