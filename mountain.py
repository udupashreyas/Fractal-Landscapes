from __future__ import division
import random
from math import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0
width, height = 700, 500

class Node:
    def __init__(self, bary1, bary2, bary3):
        self.bary1 = bary1
        self.bary2 = bary2
        self.bary3 = bary3
        self.x = None
        self.y = None
    def __eq__(self, other):
        return self.bary1 == other.bary1 and self.bary2 == other.bary2 and self.bary3 == other.bary3
    '''def __ne__(self, other)
        return not self = other'''
    
class Connection:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.midpoint_x = (node1.x + node2.x)/2
        self.midpoint_y = (node1.y + node2.y)/2
        self.length = sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)
        self.length_x = abs(node1.x - node2.x)
        self.length_y = abs(node1.y - node2.y)
    def __eq__(self, other):
        return self.node1 == other.node1 and self.node2 == other.node2

iters = 6 
r = 0.2 

a = Node(1,0,0)
a.x = 2
a.y = 0
b = Node(0,1,0)
b.x = 0
b.y = 0
c = Node(0,0,1)
c.x = 1
c.y = sqrt(3)/2
conns = [Connection(a, b), Connection(b, c), Connection(c, a)]
update = conns[:]

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def visualizeNet():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(width, height)
    glColor3f(0.0,0.0,1.0)
    for j in conns:
        a = j.node1
        b = j.node2
        draw_line(a.x*200 + 100, a.y*200 + 100, b.x*200 + 100, b.y*200 + 100)
    glutSwapBuffers()

for i in range(iters):
    new_nodes = []
    for j in conns:
        a = j.node1
        b = j.node2
        midpoint = Node((a.bary1 + b.bary1)/2, (a.bary2 + b.bary2)/2, (a.bary3 + b.bary3)/2)
        midpoint.x = j.midpoint_x + r*random.random()*j.length - r*j.length/2
        midpoint.y = j.midpoint_y + r*random.random()*j.length - r*j.length/2
        update.remove(j)
        update.append(Connection(a, midpoint))
        update.append(Connection(midpoint, b))
        new_nodes.append(midpoint)
    for j in new_nodes:
        n = Node(j.bary1 + 1/(2**(i+1)), j.bary2 - 1/(2**(i+1)), j.bary3)
        m = Node(j.bary1  + 1/(2**(i+1)), j.bary2, j.bary3 - 1/(2**(i+1)))
        k = Node(j.bary1, j.bary2 + 1/(2**(i+1)), j.bary3 - 1/(2**(i+1)))
        if n in new_nodes:
            update.append(Connection(new_nodes[new_nodes.index(n)], j))
        if m in new_nodes:
            update.append(Connection(new_nodes[new_nodes.index(m)], j))
        if k in new_nodes:
            update.append(Connection(new_nodes[new_nodes.index(k)], j))
    conns = update[:]

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
window = glutCreateWindow("mountain")
glutDisplayFunc(visualizeNet)
glutIdleFunc(visualizeNet)
glutMainLoop()
