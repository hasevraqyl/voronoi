import math as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

fulldataarray = []
n = 30000
s = 3.6 / m.sqrt(n)
dz = 2.0 / n
long = 0
z = 1 - dz / 2
k = 0
while k < (n - 1):
    r = m.sqrt(1 - z * z)
    fulldataarray.append([m.cos(long) * r, m.sin(long) * r, z])
    z = z - dz
    long = long + s / r
    k = k + 1
sphericalarray = []
for point in fulldataarray:
    c = point[0] * point[0] + point[1] * point[1] + point[2] * point[2]
    c2 = point[0] * point[0] + point[1] * point[1]
    sphericalarray.append(
        [
            m.sqrt(c),
            np.sign(point[1]) * m.acos(point[0] / m.sqrt(c2)),
            m.acos(point[2] / m.sqrt(c)),
        ]
    )
ep = 0
while ep < len(sphericalarray):
    sphericalarray[ep].pop(0)
    ep = ep + 1
finalarray = []
for point in sphericalarray:
    finalarray.append([m.pi - point[0], m.pi - point[1]])
points = np.array(finalarray)
vor = Voronoi(points, qhull_options="Qbb Qc Qz QJ")
fig = voronoi_plot_2d(vor)
art1, art2 = fig.axes[0].get_children()[0:2]
art1.set_visible(False)
art2.set_visible(False)
plt.ylim(0, m.pi)
plt.xlim(0, m.pi)
fig.set_size_inches(60, 30)
fig.set_dpi(10000)
plt.savefig("filename1")
