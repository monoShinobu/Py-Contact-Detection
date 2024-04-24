import numpy as np
import funcionesSLM as f
from vpython import *

class piramide:
    def __init__(self, pos):
        
        self.posVert = np.array([[1,-0.5,1],     #vertice 0
                                [-1,-0.5,1],     #vertice 1
                                [-1,-0.5,-1],    #vertice 2
                                [1,-0.5,-1],     #vertice 3
                                [0,1.5,0]])      #vertice 4
    
        self.vertices = np.array([[pos[0]+self.posVert[0][0],pos[1]+self.posVert[0][1],pos[2]+self.posVert[0][2]],
                                  [pos[0]+self.posVert[1][0],pos[1]+self.posVert[1][1],pos[2]+self.posVert[1][2]],
                                  [pos[0]+self.posVert[2][0],pos[1]+self.posVert[2][1],pos[2]+self.posVert[2][2]],
                                  [pos[0]+self.posVert[3][0],pos[1]+self.posVert[3][1],pos[2]+self.posVert[3][2]],
                                  [pos[0]+self.posVert[4][0],pos[1]+self.posVert[4][1],pos[2]+self.posVert[4][2]]])
        
        self.verticesArista = np.array([[0,4,5],             #vertice 0
                                        [0,1,3],             #vertice 1
                                        [1,2,6],             #vertice 2
                                        [2,4,7],             #vertice 3
                                        [6,3,5,7]])          #vertice 4
        
        self.aristas = np.array([[0,1],     #arista 0
                                 [1,2],     #arista 1
                                 [2,3],     #arista 2
                                 [4,1],     #arista 3
                                 [3,0],     #arista 4
                                 [4,0],     #arista 5
                                 [4,2],     #arista 6
                                 [4,3]])    #arista 7
                                  
        self.carasVertices = np.array([[3,2,1,0],    #cara 0
                                       [3,0,4],      #cara 1
                                       [3,4,2],      #cara 2
                                       [4,2,1],      #cara 3
                                       [4,0,1]])     #cara 4
        
        self.caras = np.array([[4,2,1,0],      #cara 0
                               [7,4,5],        #cara 1
                               [7,6,2],        #cara 2
                               [6,3,1],        #cara 3
                               [3,5,0]])       #cara 4
        
        self.vertices3D = np.array([sphere(pos = vector(self.vertices[0][0],self.vertices[0][1],self.vertices[0][2]), color = color.purple, radius = 0.1),  #0
                                    sphere(pos = vector(self.vertices[1][0],self.vertices[1][1],self.vertices[1][2]), color = color.red, radius = 0.1),     #1
                                    sphere(pos = vector(self.vertices[2][0],self.vertices[2][1],self.vertices[2][2]), color = color.blue, radius = 0.1),    #2
                                    sphere(pos = vector(self.vertices[3][0],self.vertices[3][1],self.vertices[3][2]), color = color.yellow, radius = 0.1),  #3
                                    sphere(pos = vector(self.vertices[4][0],self.vertices[4][1],self.vertices[4][2]), color = color.green, radius = 0.1)])   #4

        self.aristas3D = np.array([arrow(pos = vector(self.vertices[self.aristas[0][0]][0],self.vertices[self.aristas[0][0]][1],self.vertices[self.aristas[0][0]][2]), axis = vector(self.vertices[self.aristas[0][1]][0],self.vertices[self.aristas[0][1]][1],self.vertices[self.aristas[0][1]][2]) - vector(self.vertices[self.aristas[0][0]][0],self.vertices[self.aristas[0][0]][1],self.vertices[self.aristas[0][0]][2]), color = color.magenta, shaftwidth = 0.05), #0
                                   arrow(pos = vector(self.vertices[self.aristas[1][0]][0],self.vertices[self.aristas[1][0]][1],self.vertices[self.aristas[1][0]][2]), axis = vector(self.vertices[self.aristas[1][1]][0],self.vertices[self.aristas[1][1]][1],self.vertices[self.aristas[1][1]][2]) - vector(self.vertices[self.aristas[1][0]][0],self.vertices[self.aristas[1][0]][1],self.vertices[self.aristas[1][0]][2]), color = color.purple, shaftwidth = 0.05),  #1
                                   arrow(pos = vector(self.vertices[self.aristas[2][0]][0],self.vertices[self.aristas[2][0]][1],self.vertices[self.aristas[2][0]][2]), axis = vector(self.vertices[self.aristas[2][1]][0],self.vertices[self.aristas[2][1]][1],self.vertices[self.aristas[2][1]][2]) - vector(self.vertices[self.aristas[2][0]][0],self.vertices[self.aristas[2][0]][1],self.vertices[self.aristas[2][0]][2]), color = color.yellow, shaftwidth = 0.05),  #2
                                   arrow(pos = vector(self.vertices[self.aristas[3][0]][0],self.vertices[self.aristas[3][0]][1],self.vertices[self.aristas[3][0]][2]), axis = vector(self.vertices[self.aristas[3][1]][0],self.vertices[self.aristas[3][1]][1],self.vertices[self.aristas[3][1]][2]) - vector(self.vertices[self.aristas[3][0]][0],self.vertices[self.aristas[3][0]][1],self.vertices[self.aristas[3][0]][2]), color = color.blue, shaftwidth = 0.05),    #3
                                   arrow(pos = vector(self.vertices[self.aristas[4][0]][0],self.vertices[self.aristas[4][0]][1],self.vertices[self.aristas[4][0]][2]), axis = vector(self.vertices[self.aristas[4][1]][0],self.vertices[self.aristas[4][1]][1],self.vertices[self.aristas[4][1]][2]) - vector(self.vertices[self.aristas[4][0]][0],self.vertices[self.aristas[4][0]][1],self.vertices[self.aristas[4][0]][2]), color = color.green, shaftwidth = 0.05),   #4
                                   arrow(pos = vector(self.vertices[self.aristas[5][0]][0],self.vertices[self.aristas[5][0]][1],self.vertices[self.aristas[5][0]][2]), axis = vector(self.vertices[self.aristas[5][1]][0],self.vertices[self.aristas[5][1]][1],self.vertices[self.aristas[5][1]][2]) - vector(self.vertices[self.aristas[5][0]][0],self.vertices[self.aristas[5][0]][1],self.vertices[self.aristas[5][0]][2]), color = color.orange, shaftwidth = 0.05),  #5
                                   arrow(pos = vector(self.vertices[self.aristas[6][0]][0],self.vertices[self.aristas[6][0]][1],self.vertices[self.aristas[6][0]][2]), axis = vector(self.vertices[self.aristas[6][1]][0],self.vertices[self.aristas[6][1]][1],self.vertices[self.aristas[6][1]][2]) - vector(self.vertices[self.aristas[6][0]][0],self.vertices[self.aristas[6][0]][1],self.vertices[self.aristas[6][0]][2]), color = color.red, shaftwidth = 0.05),     #6
                                   arrow(pos = vector(self.vertices[self.aristas[7][0]][0],self.vertices[self.aristas[7][0]][1],self.vertices[self.aristas[7][0]][2]), axis = vector(self.vertices[self.aristas[7][1]][0],self.vertices[self.aristas[7][1]][1],self.vertices[self.aristas[7][1]][2]) - vector(self.vertices[self.aristas[7][0]][0],self.vertices[self.aristas[7][0]][1],self.vertices[self.aristas[7][0]][2]), color = color.cyan, shaftwidth = 0.05)])    #7

        self.numVertices = np.array([text(text ="0",pos = vector(self.vertices[0][0],self.vertices[0][1]+0.1,self.vertices[0][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="1",pos = vector(self.vertices[1][0],self.vertices[1][1]+0.1,self.vertices[1][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="2",pos = vector(self.vertices[2][0],self.vertices[2][1]-0.2,self.vertices[2][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="3",pos = vector(self.vertices[3][0],self.vertices[3][1]-0.2,self.vertices[3][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="4",pos = vector(self.vertices[4][0],self.vertices[4][1]-0.2,self.vertices[4][2]),color=color.green, height=0.2 , billboard=True)])
        
        
        #punto medio de la arista
        self.posAriMed = np.array([f.punAleaAris(np.array([self.vertices[self.aristas[0][0]],self.vertices[self.aristas[0][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[1][0]],self.vertices[self.aristas[1][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[2][0]],self.vertices[self.aristas[2][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[3][0]],self.vertices[self.aristas[3][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[4][0]],self.vertices[self.aristas[4][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[5][0]],self.vertices[self.aristas[5][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[6][0]],self.vertices[self.aristas[6][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[7][0]],self.vertices[self.aristas[7][1]]]),0.5)])
        
        #Identificamos las aristas en la particula
        self.numAristas = np.array([text(text ="0",pos = vector(self.posAriMed[0][0],self.posAriMed[0][1],self.posAriMed[0][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="1",pos = vector(self.posAriMed[1][0],self.posAriMed[1][1],self.posAriMed[1][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="2",pos = vector(self.posAriMed[2][0],self.posAriMed[2][1],self.posAriMed[2][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="3",pos = vector(self.posAriMed[3][0],self.posAriMed[3][1],self.posAriMed[3][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="4",pos = vector(self.posAriMed[4][0],self.posAriMed[4][1],self.posAriMed[4][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="5",pos = vector(self.posAriMed[5][0],self.posAriMed[5][1],self.posAriMed[5][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="6",pos = vector(self.posAriMed[6][0],self.posAriMed[6][1],self.posAriMed[6][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="7",pos = vector(self.posAriMed[7][0],self.posAriMed[7][1],self.posAriMed[7][2]),color=color.red, height=0.2 , billboard=True)])
        
        self.posCaraMed = np.array([f.punMedioCaraParticula(0, self.vertices, self.carasVertices, len(self.caras[0])),
                                   f.punMedioCaraParticula(1, self.vertices, self.carasVertices, len(self.caras[1])),
                                   f.punMedioCaraParticula(2, self.vertices, self.carasVertices, len(self.caras[2])),
                                   f.punMedioCaraParticula(3, self.vertices, self.carasVertices, len(self.caras[3])),
                                   f.punMedioCaraParticula(4, self.vertices, self.carasVertices, len(self.caras[4]))])
        
        self.posCaraPlano = np.array([f.punMedioCaraParticula(0, self.vertices, self.carasVertices, len(self.caras[0])),
                                      f.punAleaAris( np.array([self.vertices[4], f.punAleaAris( np.array( [ self.vertices[3], self.vertices[0] ] ), 0.5)]), 0.6),
                                      f.punAleaAris( np.array([self.vertices[4], f.punAleaAris( np.array( [ self.vertices[2], self.vertices[3] ] ), 0.5)]), 0.6),
                                      f.punAleaAris( np.array([self.vertices[4], f.punAleaAris( np.array( [ self.vertices[1], self.vertices[2] ] ), 0.5)]), 0.6),
                                      f.punAleaAris( np.array([self.vertices[4], f.punAleaAris( np.array( [ self.vertices[0], self.vertices[1] ] ), 0.5)]), 0.6)])
        
        #Identificamos las caras en la particula
        self.numCaras = np.array([text(text ="0",pos = vector(self.posCaraMed[0][0], self.posCaraMed[0][1] + 0.1, self.posCaraMed[0][2]),color=color.white, height=0.2 , billboard=True),
                                  text(text ="1",pos = vector(self.posCaraMed[1][0], self.posCaraMed[1][1] + 0.1, self.posCaraMed[1][2]),color=color.white, height=0.2 , billboard=True),
                                  text(text ="2",pos = vector(self.posCaraMed[2][0], self.posCaraMed[2][1] + 0.1, self.posCaraMed[2][2]),color=color.white, height=0.2 , billboard=True),
                                  text(text ="3",pos = vector(self.posCaraMed[3][0], self.posCaraMed[3][1] + 0.1, self.posCaraMed[3][2]),color=color.white, height=0.2 , billboard=True),
                                  text(text ="4",pos = vector(self.posCaraMed[4][0], self.posCaraMed[4][1] + 0.1, self.posCaraMed[4][2]),color=color.white, height=0.2 , billboard=True)])
    
    
    def delete(self):
        for i in range(len(self.vertices3D)):
            self.vertices3D[i].visible = False
        
        for i in range(len(self.aristas3D)):
            self.aristas3D[i].visible = False
        
        for i in range(len(self.numVertices)):
            self.numVertices[i].visible = False
        
        for i in range(len(self.numAristas)):
            self.numAristas[i].visible = False
        
        for i in range(len(self.numCaras)):
            self.numCaras[i].visible = False
            
    def actua(self):
        self.posCaraPlano = np.array([f.punMedioCaraParticula(0, self.vertices, self.carasVertices, len(self.caras[0])),
                                      f.punAleaAris( np.array([self.vertices[4], f.punAleaAris( np.array( [ self.vertices[3], self.vertices[0] ] ), 0.5)]), 0.6),
                                      f.punAleaAris( np.array([self.vertices[4], f.punAleaAris( np.array( [ self.vertices[2], self.vertices[3] ] ), 0.5)]), 0.6),
                                      f.punAleaAris( np.array([self.vertices[4], f.punAleaAris( np.array( [ self.vertices[1], self.vertices[2] ] ), 0.5)]), 0.6),
                                      f.punAleaAris( np.array([self.vertices[4], f.punAleaAris( np.array( [ self.vertices[0], self.vertices[1] ] ), 0.5)]), 0.6)])