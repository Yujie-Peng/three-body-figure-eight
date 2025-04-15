import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from three_body import simulate_leapfrog, total_energy, total_angular_momentum

# Initial conditions (figure-eight orbit)
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
T = steps * dt
t_eval = np.linspace(0, T, steps)

# ========== RKF45 ==========
def compute_accelerations(pos):
    acc = np.zeros_like(pos)
    for i in range(3):
        for j in range(3):
            if i != j:
                r = pos[j] - pos[i]
                dist = np.linalg.norm(r)
                acc[i] += r / dist**3
    return acc

def deriv(t, y):
    y = y.reshape(2, 3, 2)
    pos, vel = y[0], y[1]
    acc = compute_accelerations(pos)
    return np.concatenate([vel, acc]).flatten()

# Initial state for RKF
y0 = np.array([initial_positions, initial_velocities]).flatten()
sol = solve_ivp(deriv, [0, T], y0, method='RK45', t_eval=t_eval, rtol=1e-9, atol=1e-9)
rkf_positions = sol.y[:6].reshape(3, 2, -1).transpose(2, 0, 1)
rkf_velocities = sol.y[6:].reshape(3, 2, -1).transpose(2, 0, 1)

# ========== Leapfrog ==========
lf_positions, lf_velocities = simulate_leapfrog(initial_positions, initial_velocities, dt, steps)

# ========== Diagnostics ==========
def get_diagnostics(positions, velocities):
    energy = np.array([total_energy(p, v) for p, v in zip(positions, velocities)])
    ang_mom = np.array([total_angular_momentum(p, v) for p, v in zip(positions, velocities)])
    return energy, ang_mom

rkf_E, rkf_L = get_diagnostics(rkf_positions, rkf_velocities)
lf_E, lf_L = get_diagnostics(lf_positions, lf_velocities)

# ========== PLOT COMPARISONS ==========

# Energy Comparison
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(t_eval, lf_E, label="Leapfrog")
plt.plot(t_eval, rkf_E, label="RKF45", linestyle='--')
plt.title("Total Energy Over Time")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.legend()
plt.grid(True)

# Angular Momentum Comparison
plt.subplot(1, 2, 2)
plt.plot(t_eval, lf_L, label="Leapfrog")
plt.plot(t_eval, rkf_L, label="RKF45", linestyle='--')
plt.title("Total Angular Momentum Over Time")
plt.xlabel("Time")
plt.ylabel("Angular Momentum")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("../figures/rkf_vs_leapfrog_drift.png", dpi=300)
plt.show()

# Orbit Comparison (optional)
plt.figure(figsize=(6, 6))
for i in range(3):
    plt.plot(lf_positions[:, i, 0], lf_positions[:, i, 1], label=f"Leapfrog Body {i+1}")
    plt.plot(rkf_positions[:, i, 0], rkf_positions[:, i, 1], '--', label=f"RKF45 Body {i+1}")
plt.axis("equal")
plt.title("Leapfrog vs RKF45 Orbits")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../figures/trajectory_comparison.png", dpi=300)
plt.show()

