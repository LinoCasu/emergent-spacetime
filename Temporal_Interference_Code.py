import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create temporal grid
x = np.linspace(-1, 1, 500)
y = np.linspace(-1, 1, 500)
X, Y = np.meshgrid(x, y)

# Define directional angles (e.g. 5-fold symmetry)
angles = np.radians(np.arange(0, 360, 72))
np.random.seed(42)
phases = np.random.uniform(0, 2 * np.pi, len(angles))
wavelengths = np.full(len(angles), 0.1)  # fixed short wavelength

# Setup figure
fig, ax = plt.subplots()
cax = ax.imshow(np.zeros_like(X), cmap='inferno', extent=[-1, 1, -1, 1])
ax.set_title("Spacetime Interference")
ax.set_xlabel("proper time $t_x$")
ax.set_ylabel("observer time $t_y$")
ax.set_xticks([]); ax.set_yticks([])

# Animation update function
def update(frame):
    field = np.zeros_like(X)
    for i, theta in enumerate(angles):
        projection = np.cos(theta) * X + np.sin(theta) * Y
        field += np.sin(3 * np.pi * projection / wavelengths[i] + phases[i] + 0.1 * frame)
    field = np.abs(field) ** 3
    cax.set_data(field)
    cax.set_clim(np.min(field), np.max(field))
    return [cax]

# Animate
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
