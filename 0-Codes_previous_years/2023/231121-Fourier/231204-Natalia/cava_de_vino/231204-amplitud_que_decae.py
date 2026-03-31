import numpy as np
import matplotlib.pyplot as plt

omega = 0.19e-6
D = 0.0025
k = np.sqrt(omega/(2*D))
A = 20

plt.figure();
x=np.linspace(0,700,100)
V = A*np.exp(-k*x)
plt.plot(x, V)

plt.figure();
x=np.linspace(300,400,100)
V = A*np.exp(-k*x)
plt.plot(x, V)

plt.figure();
x=np.linspace(450,550,100)
V = A*np.exp(-k*x)
plt.plot(x, V)

plt.show()