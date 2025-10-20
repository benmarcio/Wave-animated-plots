import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

WAVELENGTH = 2*np.pi
E_0 = 1
WAVENUMBER = 2*np.pi/WAVELENGTH
PHASE_SHIFT = np.pi / 2
ANGULAR_FREQUENCY = 1
#test to see if it works on github
x = np.linspace(0, 16*np.pi, 250)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 16*np.pi)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)

# Remove axis ticks
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])

# Draw arrow axes
ax.quiver(0,0,0, 1,0,0,length=16*np.pi, color='k', arrow_length_ratio=0.05)
ax.quiver(0,0,0, 0,1,0, length=2, color='k', arrow_length_ratio=0.2)
ax.quiver(0,0,0, 0,0,1, length=2, color='k', arrow_length_ratio=0.4)

# Add axis labels at the arrow tips
ax.text3D(16*np.pi + 0.2, 0, 0, 'x', fontsize=12, color='k')
ax.text3D(0, 2.05, 0, 'y', fontsize=12, color='k')
ax.text3D(0, 0, 2.05, 'z', fontsize=12, color='k')

# Line objects for animation
wave_Ey, = ax.plot([], [], [], 'b', label='Electromagnetic waves Ey & Ez')
wave_Ez, = ax.plot([], [], [], 'b')
wave_Etot, = ax.plot([], [], [], 'y', label='Interference (Ey+ Ez)')
polarization_Etot, = ax.plot([], [], [], 'g', label=r'Polarization $E_{tot}$')
ax.legend()

def animate(frame):
    t = frame / 10
    k = WAVENUMBER
    w = ANGULAR_FREQUENCY
    Ey = E_0 * np.sin(k*x - w*t)
    Ez = E_0 * np.sin(k*x - w*t + PHASE_SHIFT)
    Etot = Ey +Ez
    wave_Ey.set_data(x, Ey)
    wave_Ey.set_3d_properties(np.zeros_like(x))
    
    wave_Ez.set_data(x, np.zeros_like(x))
    wave_Ez.set_3d_properties(Ez)
    
    polarization_Etot.set_data(x, Ey)       # y is Ey(x)
    polarization_Etot.set_3d_properties(Ez) # z is Ez(x)

    wave_Etot._verts3d = (x, Etot, Etot)
    
    ax.set_title(f'Interference Animation, t={t:.2f}')
    return wave_Ey, wave_Ez, wave_Etot



ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=False)
plt.show()
