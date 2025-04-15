import numpy as np
import matplotlib.pyplot as plt
from three_body import simulate_leapfrog, total_energy, total_angular_momentum

# Verified figure-eight initial conditions
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

# Run simulation
positions, velocities = simulate_leapfrog(initial_positions, initial_velocities, dt, steps)

# Track energy and angular momentum
energy = np.zeros(steps)
ang_mom = np.zeros(steps)

for i in range(steps):
    energy[i] = total_energy(positions[i], velocities[i])
    ang_mom[i] = total_angular_momentum(positions[i], velocities[i])

# Plot energy and angular momentum
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(np.arange(steps) * dt, energy)
plt.title("Total Energy Over Time")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(np.arange(steps) * dt, ang_mom)
plt.title("Total Angular Momentum Over Time")
plt.xlabel("Time")
plt.ylabel("Angular Momentum")
plt.grid(True)

plt.tight_layout()
plt.savefig("../figures/energy_momentum_drift.png", dpi=300)
plt.show()
