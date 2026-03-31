import numpy as np
import matplotlib.pyplot as plt

N_puntos=100
valores_de_x = np.linspace(-5,5,N_puntos)

fig, gfx = plt.subplots()
gfx.set_xlabel('$x$')
gfx.set_ylabel('$u(x)=tanh(x/(2\epsilon))$')
gfx.set_title('Perfil de transición de fase')

for epsilon in [1, 0.5, 0.3, 0.1]:
    valores_de_u = np.tanh(valores_de_x/(2*epsilon))
    gfx.plot(valores_de_x, valores_de_u, label='$\epsilon$ = '+ str(epsilon))

gfx.legend()
plt.show()