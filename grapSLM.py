import numpy as np
import funcionesSLM as f
from vpython import *

class grapSLM:
    def __init__(self, qi, pi):
        self.SL = np.array([sphere(pos = vector(qi[0],qi[1],qi[2]), color = color.orange, radius = 0.1, visible = False),
                            sphere(pos = vector(pi[0],pi[1],pi[2]), color = color.cyan, radius = 0.1, visible = False),
                            text(text ="Qi",pos = vector(qi[0],qi[1]+0.3,qi[2]+0.3),color=color.white, height=0.2 , billboard=True, visible = False),
                            text(text ="Pi",pos = vector(pi[0],pi[1]+0.3,pi[2]+0.3),color=color.white, height=0.2 , billboard=True, visible = False),
                            arrow(pos = vector(pi[0],pi[1],pi[2]), axis = vector(qi[0],qi[1],qi[2]) - vector(pi[0],pi[1],pi[2]), color = color.green, shaftwidth = 0.1, visible = False)])