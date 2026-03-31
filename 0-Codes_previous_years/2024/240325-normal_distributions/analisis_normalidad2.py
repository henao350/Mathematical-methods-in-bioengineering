import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Preguntar al usuario por los parámetros de la distribución
# media = float(input("Introduce la media de papel desechado por semana (kg): "))
# desviacion_estandar = float(input("Introduce la desviación estándar (kg): "))
# valor_a_contrastar = float(input("Introduce la cantidad de papel a contrastar (kg): "))
media = 4.3
desviacion_estandar = 1.9
valor_a_contrastar = 4.6
M = 20
N = 1000

# Aproximaciòn de la integral con sumas de Riemann
def f(x):
    pi = math.pi
    return (1/(desviacion_estandar*math.sqrt(2*pi)))*math.exp(
        -((x-media)/desviacion_estandar)**2/2)

delta_x = (M - valor_a_contrastar)/N
suma = 0
x_j = valor_a_contrastar
for j in range(1, N+1):         # j va a ir desde 1 hasta N
    x_j += delta_x
    suma += f(x_j)*delta_x
print(f'{suma*100:.2f} %')

# Aproximación de la integral con las librería scipy.stats de Python
z = (valor_a_contrastar - media) / desviacion_estandar
probabilidad = 1 - norm.cdf(z)
print(f'{probabilidad*100:.2f} %')

### Gráficos

x = np.linspace(media-3*desviacion_estandar, M, 100)
y = np.zeros(100)
for j in range(100):
    y[j] = f(x[j])

fig, gfx = plt.subplots(figsize=(11,6))

gfx.plot(x,y)
gfx.set_xlim(-3,M)

x = valor_a_contrastar + np.zeros(100)
y = np.linspace(0, 0.22, 100)
gfx.plot(x,y, linestyle='--')
#
x = M + np.zeros(100)
y = np.linspace(0, 0.22, 100)
gfx.plot(x,y, linestyle='--')


fig.savefig('Riemann.png')
