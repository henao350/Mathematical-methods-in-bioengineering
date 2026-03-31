import numpy as np
import matplotlib.pyplot as plt

def P(t):
    return K/(1+A*np.exp(-k*t))

N_points=100
k = 0.08
K = 1000
P_0 = 100
values_of_t = np.linspace(0, 80, N_points)

print(type(values_of_t))
print(values_of_t)

A = (K - P_0)/P_0
values_of_P = P(values_of_t)


fig, gfx = plt.subplots()
gfx.set_xlabel('$t$')
gfx.plot(values_of_t, values_of_P, color='purple')
gfx.plot(values_of_t, 0*values_of_P + 900, color='green'  )
# for epsilon in [1, 0.5, 0.3, 0.1]:
#     valores_de_u = np.tanh(values_of_t/(2*epsilon))
#     gfx.plot(values_of_t, valores_de_u, label='$\epsilon$ = '+ str(epsilon))

# gfx.set_ylabel('$u(x)=tanh(x/(2\epsilon))$')
# gfx.set_title('Perfil de transición de fase')

gfx.legend()
plt.savefig('logistic.png')

print(P(40))
print(P(80))
print(P(54))
print(P(55))
print(P(54.9))
print(P(np.array([54.97, 54.95, 54.94, 54.93, 54.935])))
