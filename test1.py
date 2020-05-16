from __future__ import annotations
from typing import List
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def thetarho(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    m= (y1-y2) / (x1-x2)
    theta= math.atan(m)
    theta= 180*theta/math.pi
    rho=abs(y1-(m*x1))/math.sqrt(m*m + 1)
    return [theta, rho]



class line:
    def __init__(self:line, a,b):
        self.a = a
        self.b = b
        self.tr = thetarho(a, b)

    def trdistance(a:line,b:line):
        dx= a.tr[0]-b.tr[0]
        dy= a.tr[1]-b.tr[1]
        return math.sqrt(dx*dx + dy*dy)

class cluster:

    def __init__(self:cluster, first:line):
        self.THRESH = 5
        self.lines=[first]

    def tryadd(self, line:line):
        for cline in self.lines:
            if cline.trdistance(line) < self.THRESH:
                self.lines.append(line)
                return True
        return False


img0 = cv2.imread('a-box.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.medianBlur(img0,5)
#ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

edges = cv2.Canny(th3, 50, 200, None, 3)
 
dst = cv2.cvtColor(img0, cv2.COLOR_GRAY2BGR)
    
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, None, 50, 10)


if lines is not None:
    for i in range(0, len(lines)):
        l = lines[i][0]
        cv2.line(dst, (l[0], l[1]), (l[2], l[3]), (0,0,255), 1, cv2.LINE_AA)


clust:List[cluster] = []

if lines is not None:
    for i in range(0, len(lines)):
        l = lines[i][0]
        ltr = line([l[0],l[1]],[l[2],l[3]])
        for c in clust:
            if c.tryadd(ltr):
                break
        else:
            clust.append(cluster(ltr))

print("num clust: ",len(clust))
plt.figure(2)

plt.imshow(edges,interpolation='bicubic')
colors = ['r', 'g', 'c']
for i,c in enumerate(clust):
    for l in c.lines:
        plt.plot([l.a[0], l.b[0]], [l.a[1], l.b[1]], colors[i%3], linewidth=2)

plt.figure(1)
colors = ['r', 'g', 'c']
for i, c in enumerate(clust):
    for l in c.lines:
        plt.plot(l.tr[0], l.tr[1], 'o', color=colors[i%3])
plt.show()
#cv2.imshow('box',img)
cv2.imshow('edges',edges)
cv2.imshow('thresh3',th3)
cv2.imshow('lines',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

##plt.imshow(edges,interpolation='bicubic')
##plt.plot([50,100], [80, 110], 'c', linewidth=5)
##plt.show()
