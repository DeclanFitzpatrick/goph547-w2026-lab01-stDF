import numpy as np
import matplotlib.pyplot as plt

from goph547lab01.gravity import (
    gravity_potential_point,
    gravity_effect_point,
)
m = 1e7
xm = np.array([0, 0, -10])
z_levels = [0, 10, 100]

# 5 m spacing: -100 to 100 with step of 5 → 41 points
x_5, y_5 = np.meshgrid(
    np.linspace(-100, 100, 41), 
    np.linspace(-100, 100, 41)
)

# 25 m spacing: -100 to 100 with step of 25 → 9 points
x_25, y_25 = np.meshgrid(
    np.linspace(-100, 100, 9), 
    np.linspace(-100, 100, 9)
)

U_5  = np.zeros((x_5.shape[0],  x_5.shape[1],  len(z_levels)))
gz_5 = np.zeros((x_5.shape[0],  x_5.shape[1],  len(z_levels)))
U_25  = np.zeros((x_25.shape[0], x_25.shape[1], len(z_levels)))
gz_25 = np.zeros((x_25.shape[0], x_25.shape[1], len(z_levels)))

print("Computing 5 m grid...")
for k, z in enumerate(z_levels):
    print(f"  z = {z} m")
    for i in range(x_5.shape[0]):
        for j in range(x_5.shape[1]):
            x = np.array([x_5[i, j], y_5[i, j], z])
            U_5[i, j, k]  = gravity_potential_point(x, xm, m)
            gz_5[i, j, k] = gravity_effect_point(x, xm, m)

print("Computing 25 m grid...")
for k, z in enumerate(z_levels):
    print(f"  z = {z} m")
    for i in range(x_25.shape[0]):
        for j in range(x_25.shape[1]):
            x = np.array([x_25[i, j], y_25[i, j], z])
            U_25[i, j, k]  = gravity_potential_point(x, xm, m)
            gz_25[i, j, k] = gravity_effect_point(x, xm, m)

Umin = min(np.min(U_5), np.min(U_25))
Umax = max(np.max(U_5), np.max(U_25))
gzmin = min(np.min(gz_5), np.min(gz_25))
gzmax = max(np.max(gz_5), np.max(gz_25))

print(f"\nGlobal ranges:")
print(f"  U:  [{Umin:.6e}, {Umax:.6e}] J/kg")
print(f"  gz: [{gzmin:.6e}, {gzmax:.6e}] m/s²")

print("\nGenerating 5 m spacing plots...")
fig, axes = plt.subplots(3, 2, figsize=(12, 16))

for k, z in enumerate(z_levels):
    # ---- Potential (left column) ----
    axU = axes[k, 0]
    cU = axU.contourf(
        x_5, y_5, U_5[:, :, k],
        levels=20, vmin=Umin, vmax=Umax, cmap="viridis"
    )
    axU.plot(x_5, y_5, "xk", markersize=2)
    cbarU = fig.colorbar(cU, ax=axU)
    cbarU.set_label("U [J/kg]", fontsize=9)
    axU.set_title(f"Gravity Potential U at z = {z} m", fontsize=11)
    axU.set_xlabel("x [m]", fontsize=10)
    axU.set_ylabel("y [m]", fontsize=10)
    axU.set_aspect("equal")
    
    # ---- Gravity effect (right column) ----
    axG = axes[k, 1]
    cG = axG.contourf(
        x_5, y_5, gz_5[:, :, k],
        levels=20, vmin=gzmin, vmax=gzmax, cmap="viridis"  
    )
    axG.plot(x_5, y_5, "xk", markersize=2)
    cbarG = fig.colorbar(cG, ax=axG)
    cbarG.set_label("gz [m/s²]", fontsize=9)
    axG.set_title(f"Gravity Effect gz at z = {z} m", fontsize=11)
    axG.set_xlabel("x [m]", fontsize=10)
    axG.set_ylabel("y [m]", fontsize=10)
    axG.set_aspect("equal")

fig.suptitle("Point Mass Gravity Fields – Grid Spacing: 5 m", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('../figures/gravity_fields_spacing_5m.png', dpi=150, bbox_inches='tight')
print("  Saved: ../figures/gravity_fields_spacing_5m.png")
plt.show()

print("Generating 25 m spacing plots...")
fig, axes = plt.subplots(3, 2, figsize=(12, 16))

for k, z in enumerate(z_levels):
    # ---- Potential (left column) ----
    axU = axes[k, 0]
    cU = axU.contourf(
        x_25, y_25, U_25[:, :, k],
        levels=20, vmin=Umin, vmax=Umax, cmap="viridis"
    )
    axU.plot(x_25, y_25, "xk", markersize=2)
    cbarU = fig.colorbar(cU, ax=axU)
    cbarU.set_label("U [J/kg]", fontsize=9)
    axU.set_title(f"Gravity Potential U at z = {z} m", fontsize=11)
    axU.set_xlabel("x [m]", fontsize=10)
    axU.set_ylabel("y [m]", fontsize=10)
    axU.set_aspect("equal")
    
    # ---- Gravity effect (right column) ----
    axG = axes[k, 1]
    cG = axG.contourf(
        x_25, y_25, gz_25[:, :, k],
        levels=20, vmin=gzmin, vmax=gzmax, cmap="viridis"
    )
    axG.plot(x_25, y_25, "xk", markersize=2)
    cbarG = fig.colorbar(cG, ax=axG)
    cbarG.set_label("gz [m/s²]", fontsize=9)
    axG.set_title(f"Gravity Effect gz at z = {z} m", fontsize=11)
    axG.set_xlabel("x [m]", fontsize=10)
    axG.set_ylabel("y [m]", fontsize=10)
    axG.set_aspect("equal")

fig.suptitle("Point Mass Gravity Fields –Grid Spacing: 25 m", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('../figures/gravity_fields_spacing_25m.png', dpi=150, bbox_inches='tight')
print("  Saved: ../figures/gravity_fields_spacing_25m.png")
plt.show()

print("\n" + "="*60)
print("="*60)