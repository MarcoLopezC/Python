import numpy as np
from matplotlib import pyplot as plt
from tabulate import tabulate




def fn(x):
    return np.e**((-x**2)+2)- x*np.sin((2*x)-3)+1

# 'f' es la funcion a evaluar
# 'a' es el limite inferior
# 'b' es el limite superior
# 'tol' es la tolerancia o margen de error aceptada ej.  1.0e-5

def FalseRule(f, a, b, tol):
    
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    x =a-(f(a)*(a-b))/(f(a)-f(b))
    ar = np.array([1, a, b,x, f(a),f(b), f(x)])
    lista = ([ar])
    idx=1
    while True:
        if (b - a) < tol or b-x < tol or x-a <tol:  
            print(x)          
            return lista
        # Utilizamos la función signo para evitar errores de precisión
        elif np.sign(f(a)) * np.sign(f(x)) > 0:
            a = x
        else:
            b = x
        x = a-(f(a)*(a-b))/(f(a)-f(b))
        idx+=1        
        lista.append([idx,a, b, x, f(a),f(b), f(x)])
    
aa =float(input('Cual es limite inferior? ')) #limite inferior
bb =float(input('Cual es la limite superior? '))#limite superior
tl=float(input('Cual es la error aceptado? ')) #1.0e-4 1.80.000001

res=FalseRule(fn, aa, bb, tl) #pasamos los parametros para iniciar la ejecucion del codigo
print(tabulate(res,["idx","a", "b", "x", "f(a)","f(b)", "f(x)"]))
#print(res)

x= np.linspace(-5,5,1000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_position('center')
ax.spines['top'].set_position('zero')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,[fn(i) for i in x])
plt.show()