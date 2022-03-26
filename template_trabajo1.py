# -*- coding: utf-8 -*-
"""
TRABAJO 1. 
Nombre Estudiante: 
"""
#%%

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#%%

'''
Esta función muestra una figura 3D con la función a optimizar junto con el 
óptimo encontrado y la ruta seguida durante la optimización. Esta función, al igual
que las otras incluidas en este documento, sirven solamente como referencia y
apoyo a los estudiantes. No es obligatorio emplearlas, y pueden ser modificadas
como se prefiera. 
    rng_val: rango de valores a muestrear en np.linspace()
    fun: función a optimizar y mostrar
    ws: conjunto de pesos (pares de valores [x,y] que va recorriendo el optimizador
                           en su búsqueda iterativa del óptimo)
    colormap: mapa de color empleado en la visualización
    title_fig: título superior de la figura
    
Ejemplo de uso: display_figure(2, E, ws, 'plasma','Ejercicio 1.2. Función sobre la que se calcula el descenso de gradiente')
'''
def display_figure(rng_val, fun, ws, colormap, title_fig):
    # https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
    from mpl_toolkits.mplot3d import Axes3D
    x = np.linspace(-rng_val, rng_val, 50)
    y = np.linspace(-rng_val, rng_val, 50)
    X, Y = np.meshgrid(x, y)
    Z = fun(X, Y) 
    fig = plt.figure()
    ax = Axes3D(fig,auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.plot_surface(X, Y, Z, edgecolor='none', rstride=1,
                            cstride=1, cmap=colormap, alpha=.6)
    if len(ws)>0:
        ws = np.asarray(ws)
        min_point = np.array([ws[-1,0],ws[-1,1]])
        min_point_ = min_point[:, np.newaxis]
        ax.plot(ws[:-1,0], ws[:-1,1], fun(ws[:-1,0], ws[:-1,1]), 'r*', markersize=5)
        ax.plot(min_point_[0], min_point_[1], fun(min_point_[0], min_point_[1]), 'r*', markersize=10)
    if len(title_fig)>0:
        fig.suptitle(title_fig, fontsize=16)
    ax.set_xlabel('u')
    ax.set_ylabel('v')
    ax.set_zlabel('E(u,v)')


#%%

np.random.seed(1)

u, v = symbols('u v', real = True)
f = (u * v * exp(-u**2 - v**2))**2

#differntiating function f in respect to a
derivada_1_u = diff(f, u)
derivada_1_v = diff(f, v)

print (derivada_1_u)
print (derivada_1_v)

print('EJERCICIO SOBRE LA BUSQUEDA ITERATIVA DE OPTIMOS\n')
print('Ejercicio 1\n')

def E(u,v):
    return ( (u * v * np.exp(-u**2 - v**2))**2 )

# Derivada parcial de E con respecto a u
def dEu(u,v):
    return -4*u**3*v**2*np.exp(-2*u**2 - 2*v**2) + 2*u*v**2*np.exp(-2*u**2 - 2*v**2)
    
# Derivada parcial de E con respecto a v
def dEv(u,v):
    return -4*u**2*v**3*np.exp(-2*u**2 - 2*v**2) + 2*u**2*v*np.exp(-2*u**2 - 2*v**2)

# Gradiente de E
def gradE(u,v):
    return np.array([dEu(u,v), dEv(u,v)])

def gradient_descent(w_ini, lr, grad_fun, fun, epsilon = None, max_iters = 50):
  
    w = w_ini
    ws = np.array(w)
    print(ws)
    # print ("w inicial: ", w)

    iteraciones = 0
    stop = False

    while (stop == False and iteraciones < max_iters):

      w = w - lr * grad_fun(w[0], w[1])
      
      ws = np.append(ws, w, axis=0
      # print ("w modificado:", w)
      iteraciones = iteraciones + 1

      evaluacion = fun(w[0], w[1])

      # print("Evaluacion a ese valor de w: ", evaluacion)

      # print (evaluacion)

      if (epsilon != None):
        stop = (evaluacion < epsilon)
      else:
        stop = False
        

    print("Paro porque ", evaluacion, "es mayor a ", epsilon, "a la iteración", iteraciones)


    print (w)
    print (ws[1])
    
    return ws, w


    
#%%

eta = 0.1 
maxIter = 10000000000
error2get = 1e-8
w_ini = np.array([0.5,-0.5])

ws, w = gradient_descent(w_ini, eta, gradE, E, error2get, maxIter)

display_figure(2, E, ws, 'plasma','Ejercicio 1.2. Función sobre la que se calcula el descenso de gradiente')

#%%

x, y = symbols('x y', real = True)
f =  x**2 + 2*y**2 + 2 * sin(2 * pi*x) * sin(pi * y)

#differntiating function f in respect to a
derivada_1_x = diff(f, x)
derivada_1_y = diff(f, y)

print (derivada_1_x)
print (derivada_1_y)

# ejercicio2. 
def f(x,y):
    return  x**2 + 2*y**2 + 2 * np.sin(2 * np.pi*x) * np.sin(np.pi * y) 
print (f(2,3))

print(np.sin(2*np.pi))

def dfx(x,y):
    return 2 * x + (4 * np.pi * np.sin(np.pi * y) * np.cos(2 * np.pi * x))

print (dfx(2,3))

def dfy(x,y):
    return 4*y + 2 * np.pi * np.sin(2* np.pi * x) * np.cos(np.pi * y)

def gradxy(x,y):
  return np.array([dfx(x,y), dfy(x,y)])

eta = 0.01 
maxIter = 50
error2get = None
w_ini = np.array([-1.0,1.0])

gradient_descent(w_ini, eta, gradxy, f, error2get, maxIter)







#%%
###############################################################################
###############################################################################
###############################################################################
###############################################################################
print('EJERCICIO SOBRE REGRESION LINEAL\n')
print('Ejercicio 1\n')

label5 = 1
label1 = -1

# Funcion para leer los datos
def readData(file_x, file_y):
	# Leemos los ficheros	
	datax = np.load(file_x)
	datay = np.load(file_y)
	y = []
	x = []	
	# Solo guardamos los datos cuya clase sea la 1 o la 5
	for i in range(0,datay.size):
		if datay[i] == 5 or datay[i] == 1:
			if datay[i] == 5:
				y.append(label5)
			else:
				y.append(label1)
			x.append(np.array([1, datax[i][0], datax[i][1]]))
			
	x = np.array(x, np.float64)
	y = np.array(y, np.float64)
	
	return x, y



#%%

# Funcion para calcular el error
def Err(x,y,w):
    w_t = np.transpose(w)
    
    predictions = np.array([np.dot(w_t, x_n) for x_n in x])
    
    error = predictions - y
    
    error_cuadratico = error * error 
    
    ecm = np.mean(error_cuadratico)
    
    return ecm


def grad_Err(x,y,w):
    
    w_t = np.transpose(w)
    
    d_w0 = np.mean( ( np.array([np.dot(w_t, x_n) for x_n in x]) - y) * x[:,0]) * 2
    d_w1 = np.mean( ( np.array([np.dot(w_t, x_n) for x_n in x]) - y) * x[:,1]) * 2
    d_w2 = np.mean( ( np.array([np.dot(w_t, x_n) for x_n in x]) - y) * x[:,2]) * 2
    
    return np.array([d_w0, d_w1, d_w2])
    
# Gradiente Descendente Estocastico
def sgd():
    #
    return w

# Pseudoinversa	
def pseudoinverse():
    #
    return w

#%%


# Lectura de los datos de entrenamiento
x, y = readData('datos/X_train.npy' , 'datos/y_train.npy' )
# Lectura de los datos para el test
x_test, y_test = readData('datos/X_test.npy', 'datos/y_test.npy')

w = np.array([1.,1.,1.])


print ('Bondad del resultado para grad. descendente estocastico:\n')
print ("Ein: ", Err(x,y,w))
print ("Eout: ", Err(x_test, y_test, w))
print ("Gradiente: ", grad_Err(x_test, y_test, w))

#Seguir haciendo el ejercicio...

print('Ejercicio 2\n')
# Simula datos en un cuadrado [-size,size]x[-size,size]
def simula_unif(N, d, size):
	return np.random.uniform(-size,size,(N,d))

def sign(x):
	if x >= 0:
		return 1
	return -1

def f(x1, x2):
	return sign((x1-0.2)**2+x2**2-0.6) 

#Seguir haciendo el ejercicio...

#%%
