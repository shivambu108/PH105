import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 20, 200)

damped = np.exp(-time/3.0) * np.sin(3*  time)

constant_amplitude = np.sin( np.pi * time)

plt.plot(time, damped, 'violet', label='damped', linestyle='dashed', marker='^')
plt.plot(time, constant_amplitude, 'green', label='constant amplitude')
plt.title('Damped and Constant Amplitude Waveforms')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
    