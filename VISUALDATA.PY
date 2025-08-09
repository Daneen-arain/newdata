import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")
plt.title("Line Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.show()
