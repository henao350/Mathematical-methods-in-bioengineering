import numpy as np
import matplotlib.pyplot as plt

# Define the function
x = np.linspace(-2, 4, 13)  # 100 points between -2 and 4
print(x)
y = x**3 - 3*x**2 + 2
print(y)
x_hires = np.linspace(-2, 4, 100)
y_hires = x_hires**3 - 3*x_hires**2 + 2

# Create the plot
plt.plot(x, y, label='$f(x) = x^3 - 3x^2 + 2$')
plt.plot(x_hires, y_hires, label='high resolution', linestyle='--', linewidth=0.5)
# plt.axhline(0, color='black', linewidth=0.8) # X-axis
plt.axvline(0, color='black', linewidth=0.8) # Y-axis
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()
plt.savefig('function_plot.png')
# plt.show()
