from math import exp, sqrt, pi
import numpy as np
import matplotlib.pyplot as plt 

def f(x):
    return 3*x**4 - (x**7/8) + 10

lower_limit = -1
upper_limit = 13
rectangles = 20
total_area = 0

delta_x = (upper_limit - lower_limit)/rectangles
for i in range(rectangles):
    x_left = lower_limit + (i)*delta_x
    x_right = lower_limit + (i+1)*delta_x
    total_area += delta_x*((f(x_right)))

print(f"Area total N=20: {total_area}")

real_value = (3/5)*13**5 - (13**8/64) + 10*13 - ((3/5)*(-1)**5 - (-1)**8/64 + 10*(-1))
print(f"Valor real N = 20: {real_value}")

relative_error = abs(real_value - total_area)/real_value
print(f"Error relativo N = 20: {relative_error*100:.3f}%")

def f(x):
    return 3*x**4 - (x**7/8) + 10

lower_limit = -1
upper_limit = 13
rectangles = 200
total_area = 0

delta_x = (upper_limit - lower_limit)/rectangles
for i in range(rectangles):
    x_left = lower_limit + (i)*delta_x
    x_right = lower_limit + (i+1)*delta_x
    total_area += delta_x*((f(x_right)))

print(f"Area total N=200: {total_area}")
real_value = (3/5)*13**5 - (13**8/64) + 10*13 - ((3/5)*(-1)**5 - (-1)**8/64 + 10*(-1))
print(f"Valor real N = 200: {real_value}")

relative_error = abs(real_value - total_area)/real_value
print(f"Error relativo N = 200: {relative_error*100:.3f}%")


def f(x):
    return 3*x**4 - (x**7/8) + 10

lower_limit = -1
upper_limit = 13
rectangles = 20000
total_area = 0

delta_x = (upper_limit - lower_limit)/rectangles
for i in range(rectangles):
    x_left = lower_limit + (i)*delta_x
    x_right = lower_limit + (i+1)*delta_x
    total_area += delta_x*((f(x_right)))

print(f"Area total N=20000: {total_area}")

real_value = (3/5)*13**5 - (13**8/64) + 10*13 - ((3/5)*(-1)**5 - (-1)**8/64 + 10*(-1))
print(f"Valor real N = 20000: {real_value}")

relative_error = abs(real_value - total_area)/real_value
print(f"Error relativo N = 20000: {relative_error*100:.15f}%")

def f(x):
    return 3*x**4 - (x**7/8) + 10

lower_limit = -1
upper_limit = 13
rectangles = 2000000
total_area = 0

delta_x = (upper_limit - lower_limit)/rectangles
for i in range(rectangles):
    x_left = lower_limit + (i)*delta_x
    x_right = lower_limit + (i+1)*delta_x
    total_area += delta_x*((f(x_right)))

print(f"Area total N=2000000: {total_area}")

real_value = (3/5)*13**5 - (13**8/64) + 10*13 - ((3/5)*(-1)**5 - (-1)**8/64 + 10*(-1))
print(f"Valor real N = 2000000: {real_value}")

relative_error = abs((real_value - total_area)/real_value)
print(f"Error relativo N = 2000000: {abs(relative_error*100):.15f}%")