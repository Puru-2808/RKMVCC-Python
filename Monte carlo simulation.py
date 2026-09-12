import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 1000

x_inside = []
y_inside = []

x_outside = []
y_outside = []

fig, ax = plt.subplots()

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect("equal")

inside_plot, = ax.plot([], [], 'o', markersize=2)
outside_plot, = ax.plot([], [], 'o', markersize=2)


def update(frame):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

    inside_plot.set_data(x_inside, y_inside)
    outside_plot.set_data(x_outside, y_outside)

    return inside_plot, outside_plot


animation = FuncAnimation(
    fig,
    update,
    frames=N,
    interval=20,
    repeat=False
)

plt.show()