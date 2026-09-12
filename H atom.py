import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Grid
# -----------------------------

x = np.linspace(-10, 10, 150)
y = np.linspace(-10, 10, 150)
z = np.linspace(-10, 10, 150)

X, Y, Z = np.meshgrid(x, y, z)

r = np.sqrt(X**2 + Y**2 + Z**2)


# -----------------------------
# Hydrogen 1s wave function
# -----------------------------

R = 2*np.exp(-r)

Y00 = 1/np.sqrt(4*np.pi)

Psi = R*Y00


# -----------------------------
# Probability density
# -----------------------------

P = np.abs(Psi)**2


# -----------------------------
# Select points for plotting
# -----------------------------

threshold = 0.02*np.max(P)

mask = P > threshold


# -----------------------------
# 3D plot
# -----------------------------

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    X[mask],
    Y[mask],
    Z[mask],
    c=P[mask],
    s=1
)

# Nucleus

ax.scatter(
    0,
    0,
    0,
    color='red',
    s=100
)

ax.set_xlabel("x (a₀)")
ax.set_ylabel("y (a₀)")
ax.set_zlabel("z (a₀)")

ax.set_title("Hydrogen 1s Orbital")

plt.show()