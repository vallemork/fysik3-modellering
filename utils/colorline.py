import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def make_segments(x, y):
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    return segments

def colorline(x, y, z=None, ax=None, cmap=plt.get_cmap('copper'), norm=plt.Normalize(0.0, 1.0), lw=1.5, alpha=1.0):
    '''
    Från https://nbviewer.org/github/dpsanders/matplotlib-examples/blob/master/colorline.ipynb

    Draws a (multi-)colored 2D line with coordinates x and y.
    The color is taken from optional data in z, and creates a LineCollection.

    z can be:
    - empty, in which case a default coloring will be used based on the position along the input arrays
    - a single number, for a uniform color [this can also be accomplished with the usual plt.plot]
    - an array of the length of at least the same length as x, to color according to this data
    - an array of a smaller length, in which case the colors are repeated along the curve

    The function colorline returns the LineCollection created, which can be modified afterwards.

    See also: plt.streamplot
    '''
    # Default colors equally spaced on [0,1]:
    if z is None: z = np.linspace(0.0, 1.0, len(x))
    if not hasattr(z, "__iter__"): z = np.array([z])
    z = np.asarray(z)
    
    segments = make_segments(x, y)
    lc = LineCollection(segments, array=z, cmap=cmap, norm=norm, linewidth=lw, alpha=alpha)

    if not ax: ax = plt.gca()
    ax.add_collection(lc)
    m = np.ptp(x) * 0.05 + 0.1
    ax.set_xlim(np.min(x) - m, np.max(x) + m)
    ax.set_ylim(np.min(y) - m, np.max(y) + m)

    return lc