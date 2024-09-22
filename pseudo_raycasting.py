#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(111, projection='3d')

# Total param
range_scale = 100.0

# Plot LiDAR cloud
num_points = 200
point_cloud_x = np.random.uniform(-range_scale/2, range_scale/2, num_points)
point_cloud_y = np.random.uniform(-range_scale/2, range_scale/2, num_points)
point_cloud_z = np.random.uniform(-range_scale/2, range_scale/2, num_points)
ax.scatter(point_cloud_x, point_cloud_y, point_cloud_z, color='orange', alpha=0.5, s=5, label="LiDAR cloud")

# Plot Map cloud at LiDAR coordinate
num_points = 1000
point_cloud_x = np.random.uniform(-range_scale/2, range_scale/2, num_points)
point_cloud_y = np.random.uniform(-range_scale/2, range_scale/2, num_points)
point_cloud_z = np.random.uniform(-range_scale/2, range_scale/2, num_points)
ax.scatter(point_cloud_x, point_cloud_y, point_cloud_z, color='green', s=5, label="Point cloud map")

# Sphere
resolution_deg = 10 #2
num_elevation_div = 180/resolution_deg
num_azimuth_div = 360/resolution_deg
u,v=np.mgrid[0:2*np.pi:complex(0,num_azimuth_div), 0:np.pi:complex(0,num_elevation_div)]
x=range_scale*np.cos(u)*np.sin(v)
y=range_scale*np.sin(u)*np.sin(v)
z=range_scale*np.cos(v)
ax.plot_wireframe(x, y, z, color='gray', linewidth=0.3)
ax.set_box_aspect([1, 1, 1])  # Equal scaling

# Plot lines from origin to each point on the wireframe
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        ax.plot([0, x[i, j]], [0, y[i, j]], [0, z[i, j]], color='gray', linewidth=0.3)

# Plot the origin (0, 0, 0) as a large black dot
ax.scatter(0, 0, 0, color='black', alpha=0.5, s=50, label="Origin(LiDAR)")  # 's' controls the size of the point

ax.grid(False)

plt.legend()
plt.show()