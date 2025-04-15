import numpy as np

G = 1.0
m = 1.0

def compute_accelerations(positions):
    acc = np.zeros_like(positions)
    for i in range(3):
        for j in range(3):
            if i != j:
                r = positions[j] - positions[i]
                dist = np.linalg.norm(r)
                acc[i] += G * m * r / dist**3
    return acc

def simulate_leapfrog(positions, velocities, dt, steps):
    pos_hist = np.zeros((steps, 3, 2))
    vel_hist = np.zeros((steps, 3, 2))

    p = np.copy(positions)
    v = np.copy(velocities)
    a = compute_accelerations(p)

    for i in range(steps):
        v += 0.5 * dt * a
        p += dt * v
        a = compute_accelerations(p)
        v += 0.5 * dt * a
        pos_hist[i] = p
        vel_hist[i] = v

    return pos_hist, vel_hist

def total_energy(positions, velocities):
    kinetic = 0.5 * m * np.sum(np.linalg.norm(velocities, axis=1)**2)
    potential = 0
    for i in range(3):
        for j in range(i+1, 3):
            r = np.linalg.norm(positions[i] - positions[j])
            potential -= G * m * m / r
    return kinetic + potential

def total_angular_momentum(positions, velocities):
    return np.sum([m * (r[0]*v[1] - r[1]*v[0]) for r, v in zip(positions, velocities)])

if __name__ == "__main__":
    # Verified figure-eight initial conditions
    positions_0 = np.array([
        [0.97000436, -0.24308753],
        [-0.97000436, 0.24308753],
        [0.0, 0.0]
    ])
    velocities_0 = np.array([
        [0.4662036850, 0.4323657300],
        [0.4662036850, 0.4323657300],
        [-0.93240737, -0.86473146]
    ])

    dt = 0.001
    steps = 20000

    positions, velocities = simulate_leapfrog(positions_0, velocities_0, dt, steps)

    E = total_energy(positions[-1], velocities[-1])
    L = total_angular_momentum(positions[-1], velocities[-1])

    print(f"Final Energy: {E:.6f}")
    print(f"Final Angular Momentum: {L:.6f}")

