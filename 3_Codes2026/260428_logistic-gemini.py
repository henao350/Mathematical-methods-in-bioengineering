import numpy as np
import matplotlib.pyplot as plt

# --- Tus parámetros originales ---
r = 0.6
K = 300
N_0 = 44
target = 250

def N(t):
    return K / (1 + ((K / N_0) - 1) * np.exp(-r * t))

# --- Implementación de Bisección ---
def biseccion(func, a, b, tol=1e-5):
    # f(t) = N(t) - 250, buscamos donde sea 0
    def f(t):
        return func(t) - target

    if f(a) * f(b) >= 0:
        print("El método de bisección falla: f(a) y f(b) deben tener signos opuestos.")
        return None

    iteracion = 0
    while (b - a) / 2.0 > tol:
        punto_medio = (a + b) / 2.0
        if f(punto_medio) == 0:
            return punto_medio # Raíz exacta encontrada
        elif f(a) * f(punto_medio) < 0:
            b = punto_medio
        else:
            a = punto_medio
        iteracion += 1
    
    return (a + b) / 2.0

# Definimos el intervalo basado en tu gráfica (0 a 12)
t_solucion = biseccion(N, 0, 12)

print(f"La solución encontrada es t = {t_solucion:.5f}")
print(f"Verificación: N({t_solucion:.5f}) = {N(t_solucion):.5f}")

# --- Gráfica para visualizar el punto ---
values_of_t = np.linspace(0, 12, 100)
plt.plot(values_of_t, N(values_of_t), color='purple', label='Logistic')
plt.axhline(y=target, color='green', linestyle='--', label='Target (250)')
plt.plot(t_solucion, target, 'ro', label=f'Intersección (t≈{t_solucion:.2f})')
plt.xlabel('$t$')
plt.ylabel('$N(t)$')
plt.legend()
plt.grid(True)
plt.show()