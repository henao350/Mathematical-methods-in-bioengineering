from math import exp, sqrt, pi

def f(z):
    return (1/sqrt(2*pi))*exp(-z**2/2)

N = 1000000
z_start = -2
z_end = 2
delta_z = (z_end - z_start)/N

sum = 0
for j in range(1,N+1):
    z_left = z_start + (j-1)*delta_z
    z_right = z_start + j*delta_z
    sum = sum + delta_z*(f(z_left) + f(z_right))/2

print(f'Suma de Riemann = {sum:.13f}')