import numpy as np
import matplotlib.pyplot as plt

def N(t):
    return K/(1+((K/N_0)-1)*np.exp(-r*t))

r = 0.6
K = 300
N_0 = 44

N_points=100
t_inicial = 0
t_final = 12
values_of_t = np.linspace(t_inicial, t_final, N_points)
values_of_N = N(values_of_t)

fig, gfx = plt.subplots()
gfx.set_xlabel('$t$')
gfx.plot(values_of_t, values_of_N, color='purple', label='Logistic')
gfx.plot(values_of_t, 0*values_of_t + 250, color='green', label='Target')
gfx.legend()
plt.savefig('logistic.png')

t=4; print(f't={t}, N={N(t):.1f}')
t=5; print(f't={t}, N={N(t):.1f}')
t=5.6; print(f't={t}, N={N(t):.1f}')
t=5.6125; print(f't={t}, N={N(t):.1f}')
t=5.617; print(f't={t}, N={N(t):.1f}')
t=5.618; print(f't={t}, N={N(t):.1f}')
t=5.625; print(f't={t}, N={N(t):.1f}')
t=5.65; print(f't={t}, N={N(t):.1f}')
t=5.7; print(f't={t}, N={N(t):.1f}')
t=6; print(f't={t}, N={N(t):.1f}')