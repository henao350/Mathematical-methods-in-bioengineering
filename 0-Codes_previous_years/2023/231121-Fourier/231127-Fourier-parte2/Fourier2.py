import numpy as np
from math import pi
from scipy import integrate
import matplotlib.pyplot as plt
from matplotlib import animation

L = 10      # largo de la barra medido en metros

N_puntos = 100
valores_de_x = np.linspace(0, L, N_puntos)

N_modos = 20;  
def aux_animacion_modos_de_Fourier(numero_de_cuadro):
    gfx.clear()
    n=int((numero_de_cuadro/numero_de_cuadros)*N_modos)+1
    gfx.set_xlabel('$x$')
    gfx.set_ylabel('$\sin($' + str(n) + '$\cdot x/L\cdot \pi)$')
    gfx.set_title('Modo de Fourier n=' + str(n))

    def funcion_auxiliar(x):
        return np.sin(n*x/L*pi)
    valores_de_y = funcion_auxiliar (valores_de_x)
    gfx.plot(valores_de_x, valores_de_y)
    # fig.savefig('modo' + str(n).zfill(2) + '.png')

numero_de_cuadros = 20
fig = plt.figure(); gfx = plt.subplot();
animacion = animation.FuncAnimation (fig, aux_animacion_modos_de_Fourier, frames=numero_de_cuadros, interval=500, repeat=False)
# https://pythonforundergradengineers.com/live-plotting-with-matplotlib.html
# plt.show()
writergif = animation.PillowWriter(fps=2)
# https://holypython.com/how-to-save-matplotlib-animations-the-ultimate-guide/
nombre_de_archivo = '1-modos_de_Fourier.gif'
animacion.save(nombre_de_archivo, writer = writergif)

###

def f(x):
    if abs(x-L/2) < 1:
        return 57
    else:
        return 0

fig = plt.figure(); gfx = plt.subplot(); 
gfx.set_xlabel('$x$')
gfx.set_ylabel('$f(x)$')
gfx.set_title('Condición inicial')

valores_de_f = np.zeros(N_puntos)

for j in range(N_puntos):
    valores_de_f[j] = f(valores_de_x[j])

gfx.plot(valores_de_x, valores_de_f)
fig.savefig('f(x).png')

###

N_modos = 100
coeficiente_de_Fourier = np.zeros(N_modos+1)
serie_de_Fourier = np.zeros([N_modos+1,N_puntos])

for n in range(1,N_modos+1):
    coeficiente_de_Fourier[n] = 2/L*(integrate.quad (lambda x : f(x)*np.sin(n*x/L*pi) ,0,  L))[0]
    serie_de_Fourier[n,:] = serie_de_Fourier[n-1,:] + coeficiente_de_Fourier[n]*np.sin(n*valores_de_x/L*pi)

def aux_animacion_serie_de_Fourier(numero_de_cuadro):
    gfx.clear()
    n=int((numero_de_cuadro/numero_de_cuadros)*N_modos)+1
    gfx.set_xlabel('$x$')
    gfx.set_title('Hasta el modo de Fourier n=' + str(n))
    valores_de_y = serie_de_Fourier[n,:]
    gfx.plot(valores_de_x, valores_de_f)
    gfx.plot(valores_de_x, valores_de_y)
    gfx.set_ylim(-10,70)

numero_de_cuadros = 50
fig = plt.figure(); gfx = plt.subplot();
animacion = animation.FuncAnimation (fig, aux_animacion_serie_de_Fourier, frames=numero_de_cuadros, interval=500, repeat=False)
writergif = animation.PillowWriter(fps=3)
nombre_de_archivo = '2-serie_de_Fourier.gif'
animacion.save(nombre_de_archivo, writer = writergif)

###

def aux_animacion_calor(numero_de_cuadro):
    gfx.clear()
    t=(numero_de_cuadro/numero_de_cuadros)*t_final
    gfx.set_xlabel('$x$')
    gfx.set_title('t=' + str(round(t,2)))
    valores_de_y = np.zeros(N_puntos)
    for n in range(N_modos+1):
        valores_de_y += coeficiente_de_Fourier[n]*np.sin(n*valores_de_x/L*pi)*np.exp(-n**2*pi**2/L**2*t)
    gfx.plot(valores_de_x, valores_de_f)
    gfx.plot(valores_de_x, valores_de_y)

numero_de_cuadros = 30; t_final = 0.2
fig = plt.figure(); gfx = plt.subplot();
animacion = animation.FuncAnimation (fig, aux_animacion_calor, frames=numero_de_cuadros, interval=500, repeat=False)
writergif = animation.PillowWriter(fps=4)
nombre_de_archivo = '3-evolucion_del_calor-camara_lenta.gif'
animacion.save(nombre_de_archivo, writer = writergif)

numero_de_cuadros = 100; t_final = 7
fig = plt.figure(); gfx = plt.subplot();
animacion = animation.FuncAnimation (fig, aux_animacion_calor, frames=numero_de_cuadros, interval=500, repeat=False)
writergif = animation.PillowWriter(fps=10)
nombre_de_archivo = '4-evolucion_del_calor-mas_rapido.gif'
animacion.save(nombre_de_archivo, writer = writergif)
