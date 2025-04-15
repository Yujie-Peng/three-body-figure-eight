# Three-Body Figure-Eight Orbit Simulation

This project numerically simulates the classical three-body problem in Newtonian gravity, focusing on the symmetric and periodic **figure-eight orbit** discovered by Chenciner and Montgomery (2000).

## 📌 Overview

The simulation was completed as the final project for PHYS5300. It demonstrates:
- High-precision reproduction of the figure-eight orbit
- Symplectic integration via the Leapfrog (Velocity Verlet) method
- Comparison with RKF45 integration to illustrate drift in non-symplectic methods
- Visualization of trajectories, energy and angular momentum conservation
- Animation of the orbit for dynamic understanding

## 📁 Project Structure
```
three_body_project/ ├── src/ # Python simulation & analysis scripts
│ ├── three_body.py
│ ├── plot_trajectories.py
│ ├── track_diagnostics.py
│ ├── compare_integrators.py
│ └── animate_orbit.py
├── figures/ # Output plots
│ ├── three_body_trajectory.png
│ ├── energy_momentum_drift.png
│ ├── rkf_vs_leapfrog_drift.png
│ ├── trajectory_comparison.png
│ └── three_body_frame.png
├── animations/
│ └── three_body_orbit.mp4
├── progress_log.tex # Full LaTeX write-up of the project
├── requirements.txt # Python dependencies
└── README.md
```
