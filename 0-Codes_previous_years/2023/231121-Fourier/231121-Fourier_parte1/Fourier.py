import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy import integrate

L = 10      # largo de la barra medido en metros

N_puntos = 100
valores_de_x = np.linspace(0, L, N_puntos)
    
for n in range(1,21):

    fig, gfx = plt.subplots()

    gfx.set_xlabel('$x$')
    gfx.set_ylabel('$\sin($' + str(n) + '$\cdot x/L\cdot \pi)$')
    gfx.set_title('Modo de Fourier n=' + str(n))

    def funcion_auxiliar(x):
        return np.sin(n*x/L*pi)
    valores_de_y = funcion_auxiliar (valores_de_x)
    gfx.plot(valores_de_x, valores_de_y)

    fig.savefig('modo' + str(n).zfill(2) + '.png')
    plt.close()


def f(x):
    if abs(x-L/2) < 1:
        return 57
    else:
        return 0

fig, gfx = plt.subplots()
 
gfx.set_xlabel('$x$')
gfx.set_ylabel('$f(x)$')
gfx.set_title('Condición inicial')

valores_de_y = np.zeros(N_puntos)
for j in range(N_puntos):
    valores_de_y[j] = f(valores_de_x[j])
gfx.plot(valores_de_x, valores_de_y)

fig.savefig('f(x).png')
plt.close()

valores_de_y = np.zeros(N_puntos)

for n in range(1,100):
    a_n = 2/L*(integrate.quad (lambda x : f(x)*np.sin(n*x/L*pi) ,0,  L))[0]
    fig, gfx = plt.subplots()
    gfx.set_xlabel('$x$')
    gfx.set_title('Hasta el modo de Fourier n=' + str(n))

    valores_de_y += a_n*np.sin(n*valores_de_x/L*pi)

    gfx.plot(valores_de_x, valores_de_y)

    fig.savefig('f_' + str(n).zfill(2) + '(x).png')
    plt.close()

