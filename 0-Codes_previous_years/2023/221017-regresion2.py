import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

t = np.array([0,4, 8,16,48]).reshape((-1,1))
X2 = np.array([0,0.637,1.397,2.737,7.523])
t_continuo = np.linspace(0,48,100)

modelo = LinearRegression()

modelo.fit(t, X2)

beta_0 = modelo.intercept_
beta_1 = modelo.coef_[0]

print("beta_0 = ", beta_0)
print("beta_1 = ", beta_1)

funCorrosion = lambda t: beta_0 + beta_1*t

plt.figure()
gfx = plt.subplot()
gfx.scatter(t, X2)
gfx.plot(t_continuo, funCorrosion(t_continuo))


plt.savefig('grafico.png')
plt.close()



