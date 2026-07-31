import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi, 500)
y = 50 * np.sin(x) - 20 * np.sin(3 * x)
y1 = 50 * np.sin(x)
y2 = -20 * np.sin(3*x)

plt.plot(x, y)
plt.plot(x, y1, color='g', label='50$\sin(x)$')
plt.plot(x, y2, color='orange', label='$-20\sin(3x)$')
plt.legend()
plt.show()


