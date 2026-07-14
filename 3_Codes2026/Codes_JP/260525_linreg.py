import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

UV_exposure = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, .0, 10.0])
lesion_chance = np.array([21.0, 45.0, 88.0, 152.0, 234.0, 355.0, 512.0, 689.0, 821.0, 945.0])

#Reshape into matrix with any number
UV_exposure = UV_exposure.reshape((np.size(UV_exposure),1))
lesion_chance = lesion_chance/100

#Create and evaluate model
modelo = LinearRegression()
modelo.fit(UV_exposure, lesion_chance)

intercept = modelo.intercept_
slope = modelo.coef_[0]
R2 = modelo.score(UV_exposure, lesion_chance)

print("intercept = ", intercept)
print("slope = ", slope)
print("R2 = ", R2)
print(f"A mouse with 6.4h of UV will have a {intercept + slope*6.4} chance to develop skin lesions")

funCorrosion = lambda t: intercept + slope*t
eyeballed = lambda t: 70 + 2800*t

rms_continuo = np.linspace(0,0.2,100)

plt.figure()
gfx = plt.subplot()
gfx.scatter(UV_exposure, lesion_chance)
gfx.plot(rms_continuo, funCorrosion(rms_continuo), color="blue", label = "Calculated")
gfx.plot(rms_continuo, eyeballed(rms_continuo), color="red", label = "eyeballed")
plt.legend()
plt.text(0.02, 488, f"Calculated: y = {slope:.2f}x + {intercept:.2f}")
plt.text(0.02, 429, f"R2 = {R2:.2f}")
plt.show()

