import numpy as np
import matplotlib.pyplot as plt
from dot_plotters import median_circle

image = np.zeros((100, 100))

for i in range(1, 50, 5):
    new_image = median_circle(image, (50, 50), i)
    plt.imshow(new_image, cmap='gray')
    plt.show()