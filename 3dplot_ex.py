# https://tech-deliberate-jiro.com/python-3dplot/

import numpy as np 
import random

def get_ball(num_points,r):
    point_cloud = []
    for i in range(num_points):
        t = random.random()
        t = np.arcsin(1-2*t)
        u= random.random() * 2 *np.pi-np.pi
        x = np.cos(t)*np.cos(u)*r
        y = np.cos(t)*np.sin(u)*r
        z= np.sin(t)*r
        point_cloud.append([x, y, z])
    return np.array(point_cloud)

#点群作成
num_points=100
r=0.5
test_data=get_ball(num_points,r)

# matplotlibで可視化
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (8, 8))
ax= fig.add_subplot(111, projection='3d')
ax.scatter(test_data[:,0],test_data[:,1],test_data[:,2], s = 1, c = "blue")
plt.show()
# fig.set_aspect('equal')

# # plotlyで可視化
# import plotly.express as px
# fig=px.scatter_3d( x=test_data[:,0],y=test_data[:,1], z=test_data[:,2])
# fig.update_traces (marker={ 'size': 1})
# fig.show()

# # Open3dで可視化
# import open3d as o3d
# pcd=o3d.geometry.PointCloud()
# pcd.points = o3d. utility.Vector3dVector(test_data) #numpy open3d に変換 
# o3d.visualization.draw_geometries([pcd])