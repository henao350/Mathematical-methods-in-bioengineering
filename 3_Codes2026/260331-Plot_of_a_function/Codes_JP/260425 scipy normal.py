#Using scipy calculate P(A<x<B)
from scipy.stats import norm

#Function to make z-score
def z_score(x, mu, sigma):
    return (x - mu) / sigma

#Mean and STD
mu = 0 #Mean
sigma = 1 #STD

#Assessed values
a = 0
b = 1

#Define the z-score of each assessed value
z_a = z_score(a, mu, sigma)
z_b = z_score(b, mu, sigma)

#Calculate the probability as phi(B) - phi(A)
prob = norm.cdf(z_b) - norm.cdf(z_a)

print(prob)