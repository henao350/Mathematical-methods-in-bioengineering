import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from matplotlib import animation
from math import pi

L = 5  # Largo de la barra en metros
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

# Perfil de temperatura inicial
def f(x):
    if 0 <= x <= 3: 
        return 5*(9-x**2)
    elif 3 < x <= 5:
        return (x**3) - 27
    else:
        return 0

valores_de_f = np.zeros(N_puntos)
for j in range(N_puntos):
    valores_de_f[j] = f(valores_de_x[j])
valores_de_x


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

### [10/07/2026] Compute what will be the temperature of the bar at x = 1.4 and t = 0.09.

for t in np.linspace(0.155,0.156,101):
    x=4.6
    # I copied the formula for the Fourier series from lines 125--134 of this code Fourier.py, adapting them appropriately.
    u=0 # The strategy to ompute the summation consists
        # in initializing as zero the variable u to which we will assign the result of the sum
        # and then add one by one (one term per each iteration of the for loop) the terms in the Fourier series formula
    for n in range(N_modos+1):
        u += coeficiente_de_Fourier[n]*np.cos(n*x/L*pi)*np.exp(-n**2*pi**2/L**2*t)
        # The above line uses the Fourier coefficients already computed in lines 63--69.
    print(f"The temperature at the point with coordinate x={x}, at the instant t={t:.5f}, will be of {u:.3f} degrees.")


x=4.6
t=0.15
skibidi = False
while skibidi == False:

    # I copied the formula for the Fourier series from lines 125--134 of this code Fourier.py, adapting them appropriately.
    u=0 # The strategy to ompute the summation consists
        # in initializing as zero the variable u to which we will assign the result of the sum
        # and then add one by one (one term per each iteration of the for loop) the terms in the Fourier series formula
    for n in range(N_modos+1):
        u += coeficiente_de_Fourier[n]*np.cos(n*x/L*pi)*np.exp(-n**2*pi**2/L**2*t)
        # The above line uses the Fourier coefficients already computed in lines 63--69.
    
    if u == 63:
        skibidi = True
        print((f"The temperature at the point with coordinate x={x}, at the instant t={t:.5f}, will be of {u:.3f} degrees."))
    elif u > 63:
        t = t + 0.000001
    elif u < 63:
        print(f"Skibidi set to true because you overshot at t={t:.5f} on u={u:.5f}")
        skibidi = True


