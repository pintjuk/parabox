from __future__ import annotations
from typing import List
import cv2
import numpy as np
import matplotlib.pyplot as plt
from Edges import *
from LineCluster import *
from Graph import *

NODE_TRESH = 20

# img0 = cv2.imread('a-box.jpg',cv2.IMREAD_GRAYSCALE)
input_img = cv2.imread('a-box-2.jpg', cv2.IMREAD_GRAYSCALE)
# img0 = cv2.imread('p-line-1.png',cv2.IMREAD_GRAYSCALE)

edges = Edges(input_img)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, None, 50, 10)
clust = lineClusters(lines, 5, 20)
graphs = ConstructGrahps(clust, NODE_TRESH)

### Subgraph Match

### Extend line into infinity

### Find vanishing points as intersections perspective lines
### draw horizon intersecting the vanashing points 
### draw y axis
#### find top and buttom planes
#### find intersection of lines from corners
#### draw y-axis internescting both centers
plt.figure(2)

plt.imshow(edges, interpolation='bicubic')
colors = ['r', 'g', 'c']
for i, c in enumerate(clust):
    for l in c.lines:
        plt.plot([l.a[0], l.b[0]], [l.a[1], l.b[1]], colors[i % 3], linewidth=2)

plt.figure(1)
colors = ['r', 'g', 'c']
for i, c in enumerate(clust):
    c.mainLine()
    for l in c.lines:
        plt.plot(l.tr[0], l.tr[1], '.', color=colors[i % 3])

plt.figure(3)

plt.imshow(edges, interpolation='bicubic')

colors = ['r', 'g', 'c']
for i, c in enumerate(clust):
    x = c.mainLine()
    plt.plot([x[0][0], x[1][0]], [x[0][1], x[1][1]], colors[i % 3], linewidth=2)

plt.show()

dst = cv2.cvtColor(input_img, cv2.COLOR_GRAY2BGR)
if lines is not None:
    for i in range(0, len(lines)):
        l = lines[i][0]
        cv2.line(dst, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 1, cv2.LINE_AA)

# cv2.imshow('box',img)
cv2.imshow('edges', edges)
cv2.imshow('lines', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

##plt.imshow(edges,interpolation='bicubic')
##plt.plot([50,100], [80, 110], 'c', linewidth=5)
##plt.show()
