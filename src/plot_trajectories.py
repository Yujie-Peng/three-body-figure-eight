import numpy as np
import matplotlib.pyplot as plt
from three_body import simulate_leapfrog

# Initial conditions must match exactly
initial_positions = np.array([
    [0.97000436, -0.24308753],
    [-0.97000436, 0.24308753],
    [0.0, 0.0]
])
initial_velocities = np.array([
    [0.4662036850, 0.4323657300],
    [0.4662036850, 0.4323657300],
    [-0.93240737, -0.86473146]
])

dt = 0.001
steps = 20000

positions, _ = simulate_leapfrog(initial_positions, initial_velocities, dt=dt, steps=steps)

colors = ['r', 'g', 'b']
labels = ['Body 1', 'Body 2', 'Body 3']

plt.figure(figsize=(8, 6))
for i in range(3):
    x = positions[:, i, 0]
    y = positions[:, i, 1]
    plt.plot(x, y, color=colors[i], label=labels[i])

plt.title("Three-Body Figure-Eight Trajectories (Leapfrog Integrator)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.tight_layout()
plt.savefig("../figures/three_body_trajectory.png", dpi=300)
plt.show()

