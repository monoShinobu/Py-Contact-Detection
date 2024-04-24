import figuras as fig
from vpython import *
import numpy as np
import time
import math as ma
    


'''
def contactoAristas(ari1, ari2):
    a = ari1[0]
    b = ari1[1]
    
    c = ari2[0]
    d = ari2[1]
    
    r = np.array(b - a)
    s = np.array(d - c)
    q = np.array(a - c)
    
    dotqr = np.dot(q, r)
    dotqs = np.dot(q, s)
    dotrs = np.dot(r, s)
    dotrr = np.dot(r, r)
    dotss = np.dot(s, s)
    
    denom = dotrr * dotss - dotrs * dotrs
    numer = dotqs * dotrs - dotqr * dotss
    
    if denom != 0:
        t = numer / denom
        u = (dotqs + t * dotrs) / dotss
    else:
        t = 2
        u = 2
    #print("\nt1 = ", t)
    #print("u = ", u,"\n")
    
    if t < 1 and t > 0:
        p0 = a + t * r
    else:
        p0 = (100,100,100)
    
    if u < 1 and u > 0:
        p1 = c + u * s
    else:
        p1 = (100,100,100)
    
    return p0, p1



arista1 = np.array([[0,0,0],[2,2,1]])
arista2 = np.array([[2,0,2],[0,2,1]])

p1 = sphere(pos = vector(arista1[0][0],arista1[0][1],arista1[0][2]), color = color.cyan, radius = 0.15)
t1 = text(text ="A",pos = vector(arista1[0][0] - 0.1,arista1[0][1] + 0.2,arista1[0][2]),color=color.black, height=0.4 , billboard=True)
p2 = sphere(pos = vector(arista1[1][0],arista1[1][1],arista1[1][2]), color = color.green, radius = 0.15)
t2 = text(text ="B",pos = vector(arista1[1][0] - 0.1,arista1[1][1] + 0.2,arista1[1][2]),color=color.black, height=0.4 , billboard=True)
a1 = arrow(pos = p1.pos, axis = p2.pos - p1.pos, color = color.red, shaftwidth = 0.1)

p3 = sphere(pos = vector(arista2[0][0],arista2[0][1],arista2[0][2]), color = color.orange, radius = 0.15)
t3 = text(text ="C",pos = vector(arista2[0][0] - 0.1,arista2[0][1] + 0.2,arista2[0][2]),color=color.black, height=0.4 , billboard=True)
p4 = sphere(pos = vector(arista2[1][0],arista2[1][1],arista2[1][2]), color = color.yellow, radius = 0.15)
t4 = text(text ="D",pos = vector(arista2[1][0] - 0.1,arista2[1][1] + 0.2,arista2[1][2]),color=color.black, height=0.4 , billboard=True)
a2 = arrow(pos = p3.pos, axis = p4.pos - p3.pos, color = color.blue, shaftwidth = 0.1)

con = contactoAristas(arista1, arista2)

p5 = sphere(pos = vector(con[0][0],con[0][1],con[0][2]), color = color.magenta, radius = 0.15)
t5 = text(text ="P",pos = vector(con[0][0] - 0.1,con[0][1] + 0.2,con[0][2]),color=color.black, height=0.4 , billboard=True)
p6 = sphere(pos = vector(con[1][0],con[1][1],con[1][2]), color = color.red, radius = 0.15)
t6 = text(text ="M",pos = vector(con[1][0] - 0.1,con[1][1]+0.1,con[1][2]+0.8),color=color.black, height=0.4 , billboard=True)
a3 = arrow(pos = p5.pos, axis = p6.pos - p5.pos, color = color.green, shaftwidth = 0.1)
'''









'''
parti1 = fig.piramide.piramide(np.array([0.0,0.0,0.0]))
p0 = sphere(pos = vector(0.0,0.0,0.0), color = color.red, radius = 0.15)

for i in range(len(parti1.numCaras)):
    parti1.numCaras[i].color = color.black

med1 = parti1.posCaraMed[0]
#p1 = sphere(pos = vector(med1[0], med1[1], med1[2]), color = color.cyan, radius = 0.15)

med2 = parti1.posCaraMed[1]
p2 = sphere(pos = vector(med2[0], med2[1], med2[2]), color = color.cyan, radius = 0.15)

pbp = box(pos = p2.pos, axis = p0.pos - p2.pos, length = 0.01, height= 5, width=5, opacity = 0.5)


med3 = parti1.posCaraMed[2]
#p3 = sphere(pos = vector(med3[0], med3[1], med3[2]), color = color.cyan, radius = 0.15)

#pbp = box(pos = p3.pos, axis = p0.pos - p3.pos, length = 0.01, height= 5, width=5, opacity = 0.5)

med4 = parti1.posCaraMed[3]
#p4 = sphere(pos = vector(med4[0], med4[1], med4[2]), color = color.cyan, radius = 0.15)

#pbp = box(pos = p4.pos, axis = p0.pos - p4.pos, length = 0.01, height= 5, width=5, opacity = 0.5)

med5 = parti1.posCaraMed[4]
#p5 = sphere(pos = vector(med5[0], med5[1], med5[2]), color = color.cyan, radius = 0.15)
'''






'''
box(pos = vector(1,1,1), color = color.red)
pyramid(pos = vector(0.5,0.05,0.5), axis = vector(0,0.5,0.8) - vector(0.5,0.05,0.5), color = color.green)
'''





    
    
'''
#cuadrado
v1 = sphere(pos = vector(1,1,1), color = color.purple, radius = 0.1)
v2 = sphere(pos = vector(-1,1,1), color = color.blue, radius = 0.1)
v3 = sphere(pos = vector(-1,1,-1), color = color.red, radius = 0.1)
v4 = sphere(pos = vector(1,1,-1), color = color.yellow, radius = 0.1)

arrow(pos = v1.pos, axis = v2.pos - v1.pos, color = color.magenta, shaftwidth = 0.05)
arrow(pos = v2.pos, axis = v3.pos - v2.pos, color = color.magenta, shaftwidth = 0.05)
arrow(pos = v3.pos, axis = v4.pos - v3.pos, color = color.magenta, shaftwidth = 0.05)
arrow(pos = v4.pos, axis = v1.pos - v4.pos, color = color.magenta, shaftwidth = 0.05)

#ac3 = box(pos = vector(0,2,0), size = vector(2,2,2), opacity = 0.5, color = color.yellow)

#box(pos = vector(0,1,0),axis = vector(0,2,0) - vector(0,1,0), length=0.01,height=2,width=2, color = color.purple)

arrow(pos = v1.pos, axis = vector(3,1,1) - v1.pos, color = color.green, shaftwidth = 0.05)
arrow(pos = v1.pos, axis = vector(1,1,3) - v1.pos, color = color.green, shaftwidth = 0.05)
arrow(pos = v1.pos, axis = vector(1,3,1) - v1.pos, color = color.green, shaftwidth = 0.05)
ac1 = box(pos = vector(2,2,2), size = vector(2,2,2), opacity = 0.5, color = color.cyan)

arrow(pos = v4.pos, axis = vector(3,1,-1) - v4.pos, color = color.red, shaftwidth = 0.05)
arrow(pos = v4.pos, axis = vector(1,3,-1) - v4.pos, color = color.red, shaftwidth = 0.05)
#ac2 = box(pos = vector(2,2,0), size = vector(2,2,2), opacity = 0.5, color = color.green)

#arrow(pos = v1.pos, axis = vector(2,0.5,2) - v1.pos, color = color.magenta, shaftwidth = 0.05)
#v5 = sphere(pos = vector(2,0.5,2), color = color.green, radius = 0.1)
'''
    
    
parti1 = fig.cubo.cubo(np.array([0.0,0.0,0.0]))
parti2 = fig.cubo.cubo(np.array([5.0,0.0,0.0]))

sphere(pos = vector(0,0,0), color = color.orange, radius = 0.1, visible = False)
sphere(pos = vector(5,0,0), color = color.cyan, radius = 0.1, visible = False)

text(text = "A", pos = vector(0,0,0), color = color.white, height = 0.5 , billboard = True)
text(text = "B", pos = vector(5,0,0), color = color.white, height = 0.5 , billboard = True)

arrow(pos = vector(0,0,0), axis = vector(5,0,0) - vector(0,0,0), color = color.green, shaftwidth = 0.05)

pbp = box(pos = vector(2.5,0,0), axis = vector(0,0,0) - vector(2.5,0,0), length = 0.01, height= 5, width=5, opacity = 0.5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    