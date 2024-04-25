import numpy as np
import matplotlib.pyplot as plt
from dot_plotters import median_circle

image = np.zeros((1000, 1000))

new_image = median_circle(image, (500, 500), 100)
plt.imshow(new_image, cmap='gray')
plt.show()