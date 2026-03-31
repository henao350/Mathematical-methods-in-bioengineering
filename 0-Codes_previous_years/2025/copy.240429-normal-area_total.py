from math import exp, sqrt, pi

def f(z):
    return exp(-z**2/2)

N = 1000000
z_inicial = -10
z_final = 10
delta_z = (z_final - z_inicial)/N

suma = 0
for j in range(1,N+1):
    z_izq = z_inicial + (j-1)*delta_z
    z_der = z_inicial + j*delta_z
    suma = suma + delta_z*(f(z_izq) + f(z_der))/2

print(f'Suma de Riemann = {suma:.13f}')