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

fig = plt.figure(); gfx = plt.subplot();
valores_de_n = range(N_modos+1)
gfx.stairs(coeficiente_de_Fourier)
gfx.set_xlabel('n')
gfx.set_ylabel('enésimo coeficiente de Fourier')
gfx.set_title('Espectro de $f(x)$')
fig.savefig('espectro.png')

####

plt.close('all')

def aux_animacion_atenuacion_modos(numero_de_cuadro):
    t=(numero_de_cuadro/numero_de_cuadros)*t_final
    gfx.clear()
    gfx.set_xlabel('x')
    gfx.set_title('t={:.2f}'.format(t))
    gfx.set_ylim(-30,30)
    for n in [1,3,5,7,9]:
        gfx.plot(valores_de_x, coeficiente_de_Fourier[n]*np.sin(n*valores_de_x/L*pi)*np.exp(-n**2*pi**2/L**2*t), label='n={}'.format(n))
    plt.legend()

numero_de_cuadros = 30; t_final = 2
fig = plt.figure(); gfx = plt.subplot();
animacion = animation.FuncAnimation (fig, aux_animacion_atenuacion_modos, frames=numero_de_cuadros, interval=500, repeat=False)
writergif = animation.PillowWriter(fps=4)
nombre_de_archivo = '5-atenuacion_modos_de_Fourier.gif'
animacion.save(nombre_de_archivo, writer = writergif)
