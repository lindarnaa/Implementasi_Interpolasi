import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk interpolasi Lagrange
def lagrange_interpolation(x, y, xi):
    n = len(x)
    yi = 0
    for i in range(n):
        li = 1
        for j in range(n):
            if i != j:
                li *= (xi - x[j]) / (x[i] - x[j])
        yi += li * y[i]
    return yi

# Generate points for plotting
x_plot = np.linspace(5, 40, 100)
y_plot_lagrange = [lagrange_interpolation(x, y, xi) for xi in x_plot]

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot_lagrange, label='Lagrange Interpolation', color='blue')
plt.scatter(x, y, color='red', label='Data Points')
plt.xlabel('Tegangan (x)')
plt.ylabel('Waktu Patah (y)')
plt.title('Interpolasi Lagrange')
plt.legend()
plt.grid(True)
plt.show()
