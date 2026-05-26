import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

alcohol_perc = np.array([0.08, 0.1, 0.12, 0.14, 0.15, 0.16, 0.18])
reaction_ms = np.array([320, 380, 440, 420, 470, 510, 630])

#Reshape into matrix with any number
alcohol_perc = alcohol_perc.reshape((np.size(alcohol_perc),1))

#Create and evaluate model
modelo = LinearRegression()
modelo.fit(alcohol_perc, reaction_ms)

intercept = modelo.intercept_
slope = modelo.coef_[0]
R2 = modelo.score(alcohol_perc, reaction_ms)

print("intercept = ", intercept)
print("slope = ", slope)
print("R2 = ", R2)
print(f"Predicted values of alcohol blood of 15% and 17% yield a {intercept + slope*0.15} and {intercept + slope*0.17} ms of reaction time, respectively")


funCorrosion = lambda t: intercept + slope*t
eyeballed = lambda t: 70 + 2800*t

rms_continuo = np.linspace(0,0.2,100)

plt.figure()
gfx = plt.subplot()
gfx.scatter(alcohol_perc, reaction_ms)
gfx.plot(rms_continuo, funCorrosion(rms_continuo), color="blue", label = "Calculated")
gfx.plot(rms_continuo, eyeballed(rms_continuo), color="red", label = "eyeballed")
plt.legend()
plt.text(0.02, 488, f"Calculated: y = {slope:.2f}x + {intercept:.2f}")
plt.text(0.02, 429, f"R2 = {R2:.2f}")
plt.show()

