import numpy as np
import matplotlib.pyplot as plt

def N(t):
    return K/(1+((K/N_0)-1)*np.exp(-r*t))

r = 0.4
K = 10000
N_0 = 500

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



t=0; print(f't={t}, N={N(t):.1f}')
t=1; print(f't={t}, N={N(t):.1f}')


t=10; print(f't={t}, N={N(t):.1f}')
t=10.1; print(f't={t}, N={N(t):.1f}')
t=10.2; print(f't={t}, N={N(t):.1f}')
t=10.3; print(f't={t}, N={N(t):.1f}')
t=10.5; print(f't={t}, N={N(t):.1f}')
t=10.75; print(f't={t}, N={N(t):.1f}')
t=10.82; print(f't={t}, N={N(t):.1f}')
t=10.825; print(f't={t}, N={N(t):.1f}')
t=10.826; print(f't={t}, N={N(t):.1f}')
t=10.8269; print(f't={t}, N={N(t):.1f}')
t=10.83; print(f't={t}, N={N(t):.1f}')
t=10.9; print(f't={t}, N={N(t):.1f}')
t=11; print(f't={t}, N={N(t):.1f}')
t=12; print(f't={t}, N={N(t):.1f}')





K=10000
N_0=500
t=1
Nt=3000

def r(t):
    return np.log(((K/Nt)-1)/((K/N_0)-1))

print(f't=1,{r(t)}')

print(np.log(0.12))

