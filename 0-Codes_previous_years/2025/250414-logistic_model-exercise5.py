import numpy as np
import matplotlib.pyplot as plt

def P(t):
    return K/(1+A*np.exp(-k*t))

P_0 = 5300  #5.3 billion in millions
k = (40-15)/P_0
K = 50000  #100 billion in millions of people

A = (K - P_0)/P_0

N_points=100

values_of_t = np.linspace(0, 510, N_points)
values_of_P = P(values_of_t)

fig, gfx = plt.subplots()
gfx.set_xlabel('$t$')
gfx.plot(values_of_t, values_of_P)

gfx.legend()
plt.savefig('logistic-World_population.png')

print(P(10))
print(P(110))
print(P(510))