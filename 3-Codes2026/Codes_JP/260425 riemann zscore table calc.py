#Adapted from Umar's

#Calculate improper integrals for normal distribution using riemann
from math import exp, sqrt, pi

#Define f(z) as the Probability density function PDF
def f(z):
    return (1/sqrt(2*pi))*exp(-z**2/2)

#Define Riemann sum parameters
n_subdivisions = 1000000 #Iterations or "rectangles"
z_start = -10 #Practical approach to -infinity
z_end = 0 #Example to get 50% to debug
dz = (z_end - z_start)/n_subdivisions

#Create empty variable to store the loop summatory
mid_sum = 0

#Loop summatory
for i in range(n_subdivisions):
    mid_x = z_start + (i + 0.5) * dz
    mid_sum += dz * f(mid_x)

print(f'Riemann approximation= {mid_sum:.13f}')
