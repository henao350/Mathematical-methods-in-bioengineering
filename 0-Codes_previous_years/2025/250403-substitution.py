from math import exp, sqrt, pi

def f(x):
    return (2 - x/3)**4

N=10000
x_start = 0
x_end = 1
delta_x = (x_end - x_start)/N

sum = 0
for j in range(1, N+1):
    x_right = x_start + j*delta_x
    x_left = x_start + (j-1)*delta_x
    sum = sum + delta_x*(f(x_left) + f(x_right))/2

print(sum)

exact_integral = (-3)*( ((5/3)**5)/5 - (2**5)/5  )

print(exact_integral)

