import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from three_body import simulate_leapfrog

# Initial conditions
r1 = [0.97000436, -0.24308753]
r2 = [-0.97000436, 0.24308753]
r3 = [0.0, 0.0]
v1 = [0.4662036850, 0.4323657300]
v2 = [0.4662036850, 0.4323657300]
v3 = [-0.93240737, -0.86473146]

initial_positions = np.array([r1, r2, r3])
initial_velocities = np.array([v1, v2, v3])

dt = 0.001
steps = 20000
positions, _ = simulate_leapfrog(initial_positions, initial_velocities, dt, steps)

# Animation setup
fig, ax = plt.subplots(figsize=(6, 6))
colors = ['r', 'g', 'b']
lines = [ax.plot([], [], color=c)[0] for c in colors]
points = [ax.plot([], [], 'o', color=c)[0] for c in colors]

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Three-Body Figure-Eight Orbit (Leapfrog)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.set_aspect("equal")

def init():
    for line, point in zip(lines, points):
        line.set_data([], [])
        point.set_data([], [])
    return lines + points

def update(frame):
    for i in range(3):
        lines[i].set_data(positions[:frame, i, 0], positions[:frame, i, 1])
        points[i].set_data([positions[frame, i, 0]], [positions[frame, i, 1]])
    return lines + points

ani = FuncAnimation(fig, update, frames=range(100, steps, 10), init_func=init, blit=True)

# Save as mp4
writer = FFMpegWriter(fps=30)
ani.save("../animations/three_body_orbit.mp4", writer=writer)
plt.close()

