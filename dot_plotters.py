# an experimental set of functions for plotting different types of dots
from typing import Tuple
import numpy as np

def median_circle(image: np.ndarray, loc: Tuple[int, int], r: int) -> np.ndarray:
    """
    Draws circle by checking the distance to the middle of a pixel

    Parameters
    ----------
    image: the image (binary)
    loc: the coordinate of the center of the circle
    r: the radius of the circle

    Returns
    -------
    The new image with the circle drawn.
    """
    # create new bigger image if necessary
    p = pad_image(image.shape, loc, r)
    next_image = np.zeros((image.shape[0] + 2*p + 1, image.shape[1] + 2*p + 1))
    circle = np.array([[1.0 if (i-r-0.5)**2 + (j-r-0.5)**2 <= r**2 else 0.0 for i in range(2*r + 1)] for j in range(2*r + 1)])
    next_image[loc[0] + p - r : loc[0] + p + r + 1, loc[1] + p - r : loc[1] + p + r + 1] = circle
    return next_image[p:p+image.shape[0], p:p+image.shape[1]]

    
    
def pad_image(shape: Tuple[int, int], location: Tuple[int, int], d: int) -> int:
    """
    If the circle to be drawn exceeds the image size, it needs to be padded.

    Parameters
    ----------
    shape: the image shape to pad (binary)
    location: the center of the circle to be drawn
    d: the distance from the center we have to worry about (sort of the radius of the circle)

    Returns
    -------
    The number of pixels to pad.
    """
    # if in top region
    candidates = []
    if location[0] - d < 0:
       candidates.append(abs(location[0] - d))
    # if in left region
    if location[1] - d < 0:
        candidates.append(abs(location[1] - d))
    # if in bottom region
    if location[0] + d > shape[0]:
        candidates.append(location[0] + d - shape[0])
    # if in right region
    if location[1] + d > shape[1]:
        candidates.append(location[1] + d - shape[1])
    return 0 if not candidates else max(candidates)