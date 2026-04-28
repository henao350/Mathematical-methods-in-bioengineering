# Create venv by exit() in vscode or directly in cmd or powershell
# cd "A:\Desktop\Cosas del doc\Metodos Matematicos\Python\Mathematical-methods-in-bioengineering" #Thats a folder in my own (JP) PC for the shared GitHub
# python -m venv .venv
# pip install "matplotlib"
# pip install "pandas"    
# Now python again in the terminal

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Requested Riemann's sum
#Defined integral from 1 to 32 of (11-(x^2)/5)^3 * 2x/5 dx
def assessed_function(x):
    return (11 - (x**2)/5)**3 * (2*x/5)

#Define the points we want to assess
point_a = 1
point_b = 32

# We use the analytical integral to compare with computed later
# u = 11 - x^2/5 → du = -(2x/5) dx
# ∫ (11 - x^2/5)^3 * (2x/5) dx = - ∫ u^3 du = -u^4/4
def integral(x):
    return -((11 - (x**2)/5)**4) / 4

#Compute
exact = integral(point_b) - integral(point_a)

# Create a list that contains all points that will be assessed
n_subdivisions = (
    list(range(1, 11)) +
    [10, 15, 20, 30, 50, 75, 100, 200, 300, 400, 500, 700, 1000, 5000, 10000, 1000000]
)

# Create an empty list to store results
results = []

#Create a for loop to iterate for each subdivision of x in the previously created list
for n in n_subdivisions:
    dx = (point_b - point_a) / n 

    #Create empty variables to store the Riemann sum
    total_left = 0
    total_mid = 0
    total_right = 0

    x = point_a
    for i in range(n):
        left_x = x
        mid_x = x + dx/2
        right_x = x + dx

        total_left  += assessed_function(left_x)  * dx
        total_mid   += assessed_function(mid_x)   * dx
        total_right += assessed_function(right_x) * dx

        x += dx


    results.append({
        "n": n,
        "dx": dx,
        "exact": exact,
        "left": total_left,
        "mid": total_mid,
        "right": total_right,
        "error_left": abs(total_left - exact),
        "error_mid": abs(total_mid - exact),
        "error_right": abs(total_right - exact),
        "perc_error_left": abs(total_left - exact) / abs(exact) * 100,
        "perc_error_mid": abs(total_mid - exact) / abs(exact) * 100,
        "perc_error_right": abs(total_right - exact) / abs(exact) * 100,
    })

# Convert to DataFrame
df = pd.DataFrame(results)

# Show table
# print(df)
df.to_csv('3_Codes2026/260331-Plot_of_a_function/Codes_JP/resultados_Riemann.csv', index=False)

# Plot errors
plt.figure()
#plt.loglog(df["n"], df["error_left"], label="Left")
#plt.loglog(df["n"], df["error_mid"], label="Mid")
#plt.loglog(df["n"], df["error_right"], label="Right")
plt.loglog(df["n"], df["perc_error_left"], label="Percentage Left")
plt.loglog(df["n"], df["perc_error_mid"], label="Percentage Mid ")
plt.loglog(df["n"], df["perc_error_right"], label="Percentage Right")
plt.xlabel("n (subdivisions)")
#plt.ylabel("Absolute Error")
plt.ylabel("Relative Error")
plt.legend()
plt.show()


# 3. Create the plot
plt.figure(figsize=(10, 6))

# Plot the continuous function
# 2. Generate smooth curve for the function
x_curve = np.linspace(point_a, point_b, 1000)
y_curve = assessed_function(x_curve)
plt.plot(x_curve, y_curve, 'r-', label='$f(x) = (11 - \\frac{x^2}{5})^3 \\cdot \\frac{2x}{5}$', linewidth=2)

# # Plot the rectangles for the Riemann Sum
# plt.bar(x_rectangles, y_rectangles, width=dx, align='edge', 
#         alpha=0.3, color='skyblue', edgecolor='blue', label=f'Riemann Sum ($n={n}$)')

# Formatting the plot
plt.title("Riemann Sum Visualization", fontsize=14)
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$f(x)$', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8) # X-axis line
# plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Show or save the plot
plt.tight_layout()
plt.savefig('riemann_sum_plot.png')
plt.show()