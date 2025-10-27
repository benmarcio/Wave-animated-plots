import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

WAVELENGTH = 2*np.pi
E_0 = 1
WAVENUMBER = 2*np.pi/WAVELENGTH
PHASE_SHIFT = np.pi / 2
ANGULAR_FREQUENCY = 0.5

x = np.linspace(0, 8*np.pi, 250)
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

ax1.set_xlim(0, 8*np.pi)
ax1.set_ylim(-4, 4)
ax1.set_zlim(-4, 4)

ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)


wave_Ey, = ax1.plot([], [], [], 'b', label=r'Electromagnetic wave $E_y$')

wave_Ez, = ax1.plot([], [], [], 'r', label=r'Electromagnetic wave $E_z$')

wave_Etot, = ax1.plot([], [], [], 'y', label=r'Interference ($E_y + E_z$)')
ax1.legend()

arrow_Ey = patches.FancyArrowPatch((0, 0), (0, 0), mutation_scale=5, color='b')
arrow_Ez = patches.FancyArrowPatch((0, 0), (0, 0), mutation_scale=5, color='r')
arrow_Etot= patches.FancyArrowPatch((0, 0), (0, 0), mutation_scale=5, color='y')

ax2.add_patch(arrow_Ey)
ax2.add_patch(arrow_Ez)
ax2.add_patch(arrow_Etot)

def animate(frame):
    t = frame / 10
    k = WAVENUMBER
    w = ANGULAR_FREQUENCY
    Ey = E_0 * np.sin(k * x - w * t)
    Ez = E_0 * np.sin(k * x - w * t + PHASE_SHIFT)
    Etot = Ey + Ez

    wave_Ey.set_data(x, Ey)
    wave_Ey.set_3d_properties(np.zeros_like(x))

    wave_Ez.set_data(x, np.zeros_like(x))
    wave_Ez.set_3d_properties(Ez)

    wave_Etot._verts3d = (x, Etot, Etot)

    ax1.set_title(f'Interference Animation, t={t:.2f}')

    ax2.clear()

    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)

    # Draw the polarization trajectories

    ax2.plot(Ey, Ez, 'g', alpha=0.5, label=r'Trajectory $E_{tot}$')
    ax2.plot(Ey, np.zeros_like(x), 'b', alpha=0.5, label=r'Trajectory $E_y$')
    ax2.plot(np.zeros_like(x), Ez, 'r', alpha=0.5, label=r'Trajectory $E_z$')

    # Update arrow position to current point (at index 0 or any fixed x)
    current_Ey = Ey[0]
    current_Ez = Ez[0]
    arrow_Etot.set_positions((0, 0), (current_Ey, current_Ez))
    arrow_Ey.set_positions((0, 0), (current_Ey, 0))
    arrow_Ez.set_positions((0, 0), (0, current_Ez))
    ax2.add_patch(arrow_Etot)
    ax2.add_patch(arrow_Ey)
    ax2.add_patch(arrow_Ez)

    ax2.set_xlabel('$E_y$')
    ax2.set_ylabel('$E_z$')
    ax2.legend()
    ax2.set_title('Polarization ellipse with vector arrow')

ani = FuncAnimation(fig, animate, frames=1000, interval=50, blit=False)
plt.show()

