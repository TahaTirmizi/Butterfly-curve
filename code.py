import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 12*np.pi, 5000)

x = np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t/12)**5)
y = np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-np.sin(t/12)**5)

plt.figure(figsize=(5,5))
plt.plot(x, y,color='black')

plt.axis('equal')
plt.show()