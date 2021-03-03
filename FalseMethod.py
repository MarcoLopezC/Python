import numpy as np
from matplotlib import pyplot as plt
from tabulate import tabulate


tl=1.0e-5

def fn(x):
    return np.e**((-x**2)+2)- x*np.sin((2*x)-3)+1
    
def FalseFunction(f, a, b, tol):
    
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
    
   

res=FalseFunction(fn, 1.8, 2, tl)
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