from __future__ import annotations

import matplotlib.pyplot as plt

from Edges import *
from Graph import *
from LineCluster import *

NODE_TRESH = 40

# input_img = cv2.imread('a-box.jpg', cv2.IMREAD_GRAYSCALE)
input_img = cv2.imread('boxPhoto1.jpg', cv2.IMREAD_GRAYSCALE)
# input_img = cv2.imread('4-lines.png',cv2.IMREAD_GRAYSCALE)
# input_img = cv2.imread('twolines.png',cv2.IMREAD_GRAYSCALE)
# input_img = cv2.imread('a-box-2.jpg', cv2.IMREAD_GRAYSCALE)
# img0 = cv2.imread('p-line-1.png',cv2.IMREAD_GRAYSCALE)

edges = Edges(input_img)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, None, 50, 10)
clust = line_clusters(lines, 10, 20)
meanlines = toLines(clust)
graphs = construct_graphs(meanlines, NODE_TRESH)

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
colors = ['r', 'g', 'c', 'y', 'm', 'w']
for i, c in enumerate(clust):
    for l in c.lines:
        plt.plot([l.a[0], l.b[0]], [l.a[1], l.b[1]], colors[i % 5], linewidth=2)

plt.figure(1)
for i, c in enumerate(clust):
    c.mainLine()
    for l in c.lines:
        plt.plot(l.lineParameters[0], l.lineParameters[1], '.', color=colors[i % 5])

plt.figure("cluster mean lines")

plt.imshow(input_img, interpolation='bicubic')

for i, c in enumerate(clust):
    x = c.mainLine()
    plt.plot([x.a[0], x.b[0]], [x.a[1], x.b[1]], colors[i % 5], linewidth=2)

plt.figure("cluster lines")

# plt.imshow(edges, interpolation='bicubic')

for i, c in enumerate(clust):
    for x in c.lines:
        plt.plot([x.a[0], x.b[0]], [x.a[1], x.b[1]], colors[i % 5], linewidth=1)

plt.figure("Graphs")
# plt.imshow(edges, interpolation='bicubic')
for i, g in enumerate(graphs):
    g.plot(plt, colors[i % 3])
plt.show()
#
dst = cv2.cvtColor(input_img, cv2.COLOR_GRAY2BGR)
cvcolors= [
    (0, 0, 255),
    (0, 255, 255),
    (255, 0, 255),
    (0, 255, 0),
    (255, 0, 0)
]
for i,g in enumerate(graphs):
    for l in g.lines:
        cv2.line(dst, (int(l[0].a[0]), int(l[0].a[1])), (int(l[0].b[0]), int(l[0].b[1])), cvcolors[i%5], 1, cv2.LINE_AA)

cv2.imshow('box', input_img)
cv2.imshow('edges', edges)
cv2.imshow('lines', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

##plt.imshow(edges,interpolation='bicubic')
##plt.plot([50,100], [80, 110], 'c', linewidth=5)
##plt.show()
