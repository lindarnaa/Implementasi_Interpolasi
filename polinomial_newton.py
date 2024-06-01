import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef

def newton_poly(coef, x_data, x):
    '''
    evaluate the newton polynomial 
    at x
    '''
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x - x_data[n-k])*p
    return p

# Data yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Menghitung koefisien divided differences
coef = divided_diff(x, y)[0, :]

# Menggunakan rentang x_new dari 5 hingga 40
x_new = np.linspace(5, 40, 500)
y_new = newton_poly(coef, x, x_new)

# Plot hasil interpolasi
plt.figure(figsize=(12, 8))
plt.plot(x, y, 'bo', label='Data Points')
plt.plot(x_new, y_new, label='Newton Interpolation')
plt.xlabel('Tegangan (x)')
plt.ylabel('Waktu Patah (y)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)
plt.show()
