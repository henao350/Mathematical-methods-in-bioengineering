import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from matplotlib import animation
from math import pi

L = 10  # Largo de la barra en metros
N_puntos = 100
valores_de_x = np.linspace(0, L, N_puntos)

# N_modos solo contendrá números impares debido a la nueva serie de solo cosenos ???
N_modos = 100

# Cambiamos la función de animación para trabajar con cosenos
def aux_animacion_modos_de_Fourier(numero_de_cuadro):
    gfx.clear()
    n = numero_de_cuadro   # Solo números impares debido a la serie de cosenos ???
    gfx.set_xlabel('$x$')
    gfx.set_ylabel('$\cos($' + str(n) + '$\cdot x/L\cdot \pi)$')
    gfx.set_title('Modo de Fourier n=' + str(n))

    def funcion_auxiliar(x):
        return np.cos(n * x / L * np.pi)

    valores_de_y = funcion_auxiliar(valores_de_x)
    gfx.plot(valores_de_x, valores_de_y)


numero_de_cuadros = 20
fig = plt.figure()
gfx = plt.subplot()
animacion = animation.FuncAnimation(fig, aux_animacion_modos_de_Fourier, frames=numero_de_cuadros, interval=500,
                                    repeat=False)
nombre_de_archivo = 'modos_de_Fourier_calor.gif'
animacion.save(nombre_de_archivo, writer='pillow', fps=2)


# Actualizamos la función f para la nueva distribución inicial de temperatura
def f(x):
    if 3 <= x <= 5:  # 2 metros en la mitad de la barra
        return 57*x
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

# Actualizamos la serie de Fourier para trabajar solo con cosenos
coeficiente_de_Fourier = np.zeros(N_modos + 1)
serie_de_Fourier = np.zeros([N_modos + 1, N_puntos])

for n in range(N_modos + 1):
    coeficiente_de_Fourier[n] = 2 / L * integrate.quad(lambda x: f(x) * np.cos(n * x / L * np.pi), 0, L)[0]
    if n==0:
        coeficiente_de_Fourier[n] /= 2    
    serie_de_Fourier[n, :] =  coeficiente_de_Fourier[n] * np.cos(n * valores_de_x / L * np.pi)
    if n>=1:
        serie_de_Fourier[n,:] += serie_de_Fourier[n-1,:]

### animacion serie de Fourier ###
def aux_animacion_serie_de_Fourier(numero_de_cuadro):
    gfx.clear()
    n=int(((numero_de_cuadro+1)/numero_de_cuadros)*(N_modos-1))
    gfx.set_xlabel('$x$')
    gfx.set_title('Hasta el modo de Fourier n=' + str(n))
    valores_de_y = serie_de_Fourier[n,:]
    gfx.plot(valores_de_x, valores_de_f)
    gfx.plot(valores_de_x, valores_de_y)
    gfx.set_ylim(-70,300)

numero_de_cuadros = 50
fig = plt.figure(); gfx = plt.subplot();
animacion = animation.FuncAnimation (fig, aux_animacion_serie_de_Fourier, frames=numero_de_cuadros, interval=500, repeat=False)
writergif = animation.PillowWriter(fps=3)
nombre_de_archivo = '2-serie_de_Fourier.gif'
animacion.save(nombre_de_archivo, writer = writergif)

### gráfico del espectro ###
fig = plt.figure()
gfx = plt.subplot()
valores_de_n = range(N_modos + 1)
gfx.stairs(coeficiente_de_Fourier)
gfx.set_xlabel('n')
gfx.set_ylabel('enésimo coeficiente de Fourier')
gfx.set_title('Espectro de $f(x)$')
nombre_de_archivo = 'espectro_calor.png'
fig.savefig(nombre_de_archivo)

# Animación para la atenuación de los modos de Fourier
def aux_animacion_atenuacion_modos(numero_de_cuadro):
    t = (numero_de_cuadro / numero_de_cuadros) * t_final
    gfx.clear()
    gfx.set_xlabel('x')
    gfx.set_title('t={:.2f}'.format(t))
    gfx.set_ylim(-100, 100)  # Puedes ajustar según sea necesario
    for n in range(1, 9 + 1):
        gfx.plot(valores_de_x, coeficiente_de_Fourier[n] * np.cos(n * valores_de_x / L * np.pi) *
                 np.exp(-n ** 2 * np.pi ** 2 / L ** 2 * t), label='n={}'.format(n))
    plt.legend()


numero_de_cuadros = 30
t_final = 2
fig = plt.figure()
gfx = plt.subplot()
animacion = animation.FuncAnimation(fig, aux_animacion_atenuacion_modos, frames=numero_de_cuadros, interval=500,
                                    repeat=False)
nombre_de_archivo = 'atenuacion_modos_de_Fourier_calor.gif'
animacion.save(nombre_de_archivo, writer='pillow', fps=4)

### Propagación del calor

def aux_animacion_calor(numero_de_cuadro):
    gfx.clear()
    t=(numero_de_cuadro/numero_de_cuadros)*t_final
    gfx.set_xlabel('$x$')
    gfx.set_title('t=' + str(round(t,2)))
    valores_de_y = np.zeros(N_puntos)
    for n in range(N_modos+1):
        valores_de_y += coeficiente_de_Fourier[n]*np.cos(n*valores_de_x/L*pi)*np.exp(-n**2*pi**2/L**2*t)
    gfx.plot(valores_de_x, valores_de_f)
    gfx.plot(valores_de_x, valores_de_y)
    gfx.set_ylim(0,300)

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
