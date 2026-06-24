#Code to calculate P(A < x < B) without scipy
import math

#Defines phi as Cumulative Density Function CDF, the function that gives origin to the z-value to probability conversion
def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

#Define average and standard deviation
mu = 0 #Mean Insert 
sigma = 1 #STD Insert 

#Defines the calculated values
a = 0 #Insert 
b = 1 #Insert

z_a = (a - mu) / sigma #Calculates Z-score for A
z_b = (b - mu) / sigma #Calculates Z-score for B

prob = phi(z_b) - phi(z_a) #Calculates P(A < x < B)

print(prob)