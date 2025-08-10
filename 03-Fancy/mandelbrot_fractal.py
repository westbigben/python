# Generate and display a Mandelbrot fractal using matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Image size (pixels) and plot limits
width, height = 800, 800
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

# Generate complex number grid
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

# Mandelbrot iteration
Z = np.zeros_like(C)
iterations = 100
mask = np.full(C.shape, True, dtype=bool)

for i in range(iterations):
    Z[mask] = Z[mask] ** 2 + C[mask]
    mask[np.abs(Z) > 2] = False

# Plot
plt.imshow(mask, extent=(xmin, xmax, ymin, ymax), cmap="twilight_shifted")
plt.title("Mandelbrot Fractal")
plt.xlabel("Real axis")
plt.ylabel("Imaginary axis")
plt.show()