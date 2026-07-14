import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#####P1
UV_exposure = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
lesion_chance = np.array([0.0210, 0.0450, 0.0880, 0.1520, 0.2340, 0.3550, 0.5120, 0.6890, 0.8210, 0.9450])

#Reshape into matrix with any number
UV_exposure = UV_exposure.reshape((np.size(UV_exposure),1))

#Create and evaluate model
modelo = LinearRegression()
modelo.fit(UV_exposure, lesion_chance)

intercept = modelo.intercept_
slope = modelo.coef_[0]
R2 = modelo.score(UV_exposure, lesion_chance)

#####P2
print("intercept = ", intercept)
print("slope = ", slope)
print("R2 = ", R2)
print(f"A mouse with 6.4h of UV will have a {intercept + slope*6.4} chance to develop skin lesions")

predicted_UV = (intercept + slope*6.4)
p5_slope_fast = slope*0.7 + slope

funCorrosion = lambda t: intercept + slope*t
funCorrosion2 = lambda t: intercept + (slope*0.7 + slope)*t
print(f"70% faster slope is {slope*0.7 + slope}")
rms_continuo = np.linspace(0,11,100)

#####5.2 hand calculated inverse function
print(f"97% chance of skin lesion is developed at 6.4 UV exposure hours with accelerated model")

plt.figure()
gfx = plt.subplot()
gfx.scatter(UV_exposure, lesion_chance)
gfx.plot(rms_continuo, funCorrosion(rms_continuo), color="blue", label = "Model")
gfx.plot(rms_continuo, funCorrosion2(rms_continuo), color="red", label = "P5 model")
gfx.scatter(UV_exposure, lesion_chance)
gfx.scatter(6.4, predicted_UV, colorizer= "green")
gfx.scatter(6.3, 0.95, colorizer= "purple")
gfx.legend()
gfx.text(0.02, 1.5, f"Model: y = {slope:.4f}x + {intercept:.4f}")
gfx.text(0.02, 1.4, f"70% faster model: y = {p5_slope_fast:.4f}x + {intercept:.4f}")
gfx.text(0.02, 1.3, f"R2 = {R2:.4f}")
gfx.text(0.02, 1.2, f"Predicted at 6.4h = {predicted_UV:.4f}")
gfx.text(0.02, 1.1, f"P5 95% chance of lesionn at {(0.95+0.2123)/0.1850:.1f} hours")
plt.show()




