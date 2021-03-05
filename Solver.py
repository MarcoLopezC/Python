# importar librerias
import math
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from tabulate import tabulate

# funcion
def f1(x):
    # funcion
    return math.e**(-(x**2) + 2) - x * math.sin(2*x - 3) + 1

# definimos la variable
a =float(input('Cual es limite inferior? ')) #limite inferior
b =float(input('Cual es la limite superior? '))#limite superior
e=float(input('Cual es la error aceptado? ')) #1.0e-4 1.80.000001
xm = (a + b) / 2  # biseccion
fa=f1(a)
fb=f1(b)
fxm=f1(xm)
ea=abs(fxm) #error actual
#datos de la estructura
n=1
arreglo=([1, a ,b ,xm ,fa ,fb ,fxm , ea ]) #arreglo
valores=([arreglo])  #lista del areglo objeto

#datos a imprimir
while (ea>=e):
    if xm*fxm < 0.0:        
        b = xm        
    else:
        a=xm  
    xmm = xm
    xm=(a+b)/2
    fa= f1(a)
    fb= f1(b)
    fxm= f1(xm)
    ea =abs(xm-xmm)
    n+=1
    valores.append([n,a,b,xm,fa,fb,fxm,ea])    


#imprime la tabla de valores

print(tabulate(valores,['#','a','b','xm','f(a)','f(b)','f(xm)','Error']))

   # configura os ejes del centro

x = np.linspace(-5,5,1000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_position('center')
ax.spines['top'].set_position('zero')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#Trazar la funcion
plt.plot(x,[f1(i) for i in x])
plt.show()