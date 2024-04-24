import numpy as np
import funcionesSLM as f
from vpython import *

class cubo:
    def __init__(self, pos):
        self.posVert = np.array([[1,1,1],      #vertice 0
                                [1,1,-1],     #vertice 1
                                [1,-1,-1],    #vertice 2
                                [1,-1,1],     #vertice 3
                                [-1,-1,-1],   #vertice 4
                                [-1,-1,1],    #vertice 5
                                [-1,1,1],     #vertice 6
                                [-1,1,-1]])   #vertice 7
        #posicion de los vertices globales con respecto al centroide
                            
        #EX Va
        self.vertices = np.array([[pos[0]+self.posVert[0][0],pos[1]+self.posVert[0][1],pos[2]+self.posVert[0][2]],
                                  [pos[0]+self.posVert[1][0],pos[1]+self.posVert[1][1],pos[2]+self.posVert[1][2]],
                                  [pos[0]+self.posVert[2][0],pos[1]+self.posVert[2][1],pos[2]+self.posVert[2][2]],
                                  [pos[0]+self.posVert[3][0],pos[1]+self.posVert[3][1],pos[2]+self.posVert[3][2]],
                                  [pos[0]+self.posVert[4][0],pos[1]+self.posVert[4][1],pos[2]+self.posVert[4][2]],
                                  [pos[0]+self.posVert[5][0],pos[1]+self.posVert[5][1],pos[2]+self.posVert[5][2]],
                                  [pos[0]+self.posVert[6][0],pos[1]+self.posVert[6][1],pos[2]+self.posVert[6][2]],
                                  [pos[0]+self.posVert[7][0],pos[1]+self.posVert[7][1],pos[2]+self.posVert[7][2]]])
        #Generamos los vetices en base a nuestro centroide de la particula
        
        self.verticesArista = np.array([[0,3,10],            #vertice 0
                                        [0,1,4],             #vertice 1
                                        [1,2,6],             #vertice 2
                                        [3,11,2],            #vertice 3
                                        [5,6,9],             #vertice 4
                                        [9,8,11],            #vertice 5
                                        [7,10,8],            #vertice 6
                                        [5,7,4]])            #vertice 7
        
        self.aristas = np.array([[0,1],#arista 0
                                 [1,2],#arista 1
                                 [2,3],#arista 2
                                 [3,0],#arista 3
                                 [1,7],#arista 4   vertices[aristas[verticesArista[numVertA][i]][0]], vertices[aristas[verticesArista[numVertA][i]][1]] 
                                 [4,7],#arista 5
                                 [4,2],#arista 6
                                 [7,6],#arista 7
                                 [6,5],#arista 8
                                 [5,4],#arista 9
                                 [6,0],#arista 10
                                 [3,5]])#arista 11
        #aristas particula
        
        self.carasVertices = np.array([[0,1,2,3],     #cara 0
                                       [1,7,4,2],     #cara 1
                                       [7,6,5,4],     #cara 2
                                       [6,0,3,5],     #cara 3
                                       [5,4,2,3],     #cara 4
                                       [7,6,0,1]])    #cara 5
        
        self.caras = np.array([[0,1,2,3],   #cara 0 
                               [4,5,6,1],   #cara 1
                               [7,8,9,5],   #cara 2
                               [10,3,11,8], #cara 3
                               [9,11,2,6],  #cara 4
                               [7,4,0,10]]) #cara 5
        #caras de las particulas
        
        self.vertices3D = np.array([sphere(pos = vector(self.vertices[0][0],self.vertices[0][1],self.vertices[0][2]), color = color.purple, radius = 0.1),
                                    sphere(pos = vector(self.vertices[1][0],self.vertices[1][1],self.vertices[1][2]), color = color.red, radius = 0.1),
                                    sphere(pos = vector(self.vertices[2][0],self.vertices[2][1],self.vertices[2][2]), color = color.blue, radius = 0.1),
                                    sphere(pos = vector(self.vertices[3][0],self.vertices[3][1],self.vertices[3][2]), color = color.yellow, radius = 0.1),
                                    sphere(pos = vector(self.vertices[4][0],self.vertices[4][1],self.vertices[4][2]), color = color.green, radius = 0.1),
                                    sphere(pos = vector(self.vertices[5][0],self.vertices[5][1],self.vertices[5][2]), color = color.cyan, radius = 0.1),
                                    sphere(pos = vector(self.vertices[6][0],self.vertices[6][1],self.vertices[6][2]), color = color.magenta, radius = 0.1),
                                    sphere(pos = vector(self.vertices[7][0],self.vertices[7][1],self.vertices[7][2]), color = color.white, radius = 0.1)])
        #vertices de la particula A mostrados por pantalla
        
        self.aristas3D = np.array([arrow(pos = vector(self.vertices[self.aristas[0][0]][0],self.vertices[self.aristas[0][0]][1],self.vertices[self.aristas[0][0]][2]), axis = vector(self.vertices[self.aristas[0][1]][0],self.vertices[self.aristas[0][1]][1],self.vertices[self.aristas[0][1]][2]) - vector(self.vertices[self.aristas[0][0]][0],self.vertices[self.aristas[0][0]][1],self.vertices[self.aristas[0][0]][2]), color = color.magenta, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[1][0]][0],self.vertices[self.aristas[1][0]][1],self.vertices[self.aristas[1][0]][2]), axis = vector(self.vertices[self.aristas[1][1]][0],self.vertices[self.aristas[1][1]][1],self.vertices[self.aristas[1][1]][2]) - vector(self.vertices[self.aristas[1][0]][0],self.vertices[self.aristas[1][0]][1],self.vertices[self.aristas[1][0]][2]), color = color.purple, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[2][0]][0],self.vertices[self.aristas[2][0]][1],self.vertices[self.aristas[2][0]][2]), axis = vector(self.vertices[self.aristas[2][1]][0],self.vertices[self.aristas[2][1]][1],self.vertices[self.aristas[2][1]][2]) - vector(self.vertices[self.aristas[2][0]][0],self.vertices[self.aristas[2][0]][1],self.vertices[self.aristas[2][0]][2]), color = color.yellow, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[3][0]][0],self.vertices[self.aristas[3][0]][1],self.vertices[self.aristas[3][0]][2]), axis = vector(self.vertices[self.aristas[3][1]][0],self.vertices[self.aristas[3][1]][1],self.vertices[self.aristas[3][1]][2]) - vector(self.vertices[self.aristas[3][0]][0],self.vertices[self.aristas[3][0]][1],self.vertices[self.aristas[3][0]][2]), color = color.blue, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[4][0]][0],self.vertices[self.aristas[4][0]][1],self.vertices[self.aristas[4][0]][2]), axis = vector(self.vertices[self.aristas[4][1]][0],self.vertices[self.aristas[4][1]][1],self.vertices[self.aristas[4][1]][2]) - vector(self.vertices[self.aristas[4][0]][0],self.vertices[self.aristas[4][0]][1],self.vertices[self.aristas[4][0]][2]), color = color.green, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[5][0]][0],self.vertices[self.aristas[5][0]][1],self.vertices[self.aristas[5][0]][2]), axis = vector(self.vertices[self.aristas[5][1]][0],self.vertices[self.aristas[5][1]][1],self.vertices[self.aristas[5][1]][2]) - vector(self.vertices[self.aristas[5][0]][0],self.vertices[self.aristas[5][0]][1],self.vertices[self.aristas[5][0]][2]), color = color.orange, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[6][0]][0],self.vertices[self.aristas[6][0]][1],self.vertices[self.aristas[6][0]][2]), axis = vector(self.vertices[self.aristas[6][1]][0],self.vertices[self.aristas[6][1]][1],self.vertices[self.aristas[6][1]][2]) - vector(self.vertices[self.aristas[6][0]][0],self.vertices[self.aristas[6][0]][1],self.vertices[self.aristas[6][0]][2]), color = color.red, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[7][0]][0],self.vertices[self.aristas[7][0]][1],self.vertices[self.aristas[7][0]][2]), axis = vector(self.vertices[self.aristas[7][1]][0],self.vertices[self.aristas[7][1]][1],self.vertices[self.aristas[7][1]][2]) - vector(self.vertices[self.aristas[7][0]][0],self.vertices[self.aristas[7][0]][1],self.vertices[self.aristas[7][0]][2]), color = color.white, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[8][0]][0],self.vertices[self.aristas[8][0]][1],self.vertices[self.aristas[8][0]][2]), axis = vector(self.vertices[self.aristas[8][1]][0],self.vertices[self.aristas[8][1]][1],self.vertices[self.aristas[8][1]][2]) - vector(self.vertices[self.aristas[8][0]][0],self.vertices[self.aristas[8][0]][1],self.vertices[self.aristas[8][0]][2]), color = color.cyan, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[9][0]][0],self.vertices[self.aristas[9][0]][1],self.vertices[self.aristas[9][0]][2]), axis = vector(self.vertices[self.aristas[9][1]][0],self.vertices[self.aristas[9][1]][1],self.vertices[self.aristas[9][1]][2]) - vector(self.vertices[self.aristas[9][0]][0],self.vertices[self.aristas[9][0]][1],self.vertices[self.aristas[9][0]][2]), color = color.blue, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[10][0]][0],self.vertices[self.aristas[10][0]][1],self.vertices[self.aristas[10][0]][2]), axis = vector(self.vertices[self.aristas[10][1]][0],self.vertices[self.aristas[10][1]][1],self.vertices[self.aristas[10][1]][2]) - vector(self.vertices[self.aristas[10][0]][0],self.vertices[self.aristas[10][0]][1],self.vertices[self.aristas[10][0]][2]), color = color.green, shaftwidth = 0.05),
                                  arrow(pos = vector(self.vertices[self.aristas[11][0]][0],self.vertices[self.aristas[11][0]][1],self.vertices[self.aristas[11][0]][2]), axis = vector(self.vertices[self.aristas[11][1]][0],self.vertices[self.aristas[11][1]][1],self.vertices[self.aristas[11][1]][2]) - vector(self.vertices[self.aristas[11][0]][0],self.vertices[self.aristas[11][0]][1],self.vertices[self.aristas[11][0]][2]), color = color.orange, shaftwidth = 0.05)])
        #aristas de la particula A mostradas por pantalla
        
        #Identificamos los vertices en la particula
        self.numVertices = np.array([text(text ="0",pos = vector(self.vertices[0][0],self.vertices[0][1]+0.1,self.vertices[0][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="1",pos = vector(self.vertices[1][0],self.vertices[1][1]+0.1,self.vertices[1][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="2",pos = vector(self.vertices[2][0],self.vertices[2][1]-0.2,self.vertices[2][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="3",pos = vector(self.vertices[3][0],self.vertices[3][1]-0.2,self.vertices[3][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="4",pos = vector(self.vertices[4][0],self.vertices[4][1]-0.2,self.vertices[4][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="5",pos = vector(self.vertices[5][0],self.vertices[5][1]-0.2,self.vertices[5][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="6",pos = vector(self.vertices[6][0],self.vertices[6][1]+0.1,self.vertices[6][2]),color=color.green, height=0.2 , billboard=True),
                                     text(text ="7",pos = vector(self.vertices[7][0],self.vertices[7][1]+0.1,self.vertices[7][2]),color=color.green, height=0.2 , billboard=True)])
        
        #punto medio de la arista
        self.posAriMed = np.array([f.punAleaAris(np.array([self.vertices[self.aristas[0][0]],self.vertices[self.aristas[0][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[1][0]],self.vertices[self.aristas[1][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[2][0]],self.vertices[self.aristas[2][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[3][0]],self.vertices[self.aristas[3][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[4][0]],self.vertices[self.aristas[4][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[5][0]],self.vertices[self.aristas[5][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[6][0]],self.vertices[self.aristas[6][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[7][0]],self.vertices[self.aristas[7][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[8][0]],self.vertices[self.aristas[8][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[9][0]],self.vertices[self.aristas[9][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[10][0]],self.vertices[self.aristas[10][1]]]),0.5),
                                   f.punAleaAris(np.array([self.vertices[self.aristas[11][0]],self.vertices[self.aristas[11][1]]]),0.5)])
        
        #Identificamos las aristas en la particula
        self.numAristas = np.array([text(text ="0",pos = vector(self.posAriMed[0][0],self.posAriMed[0][1],self.posAriMed[0][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="1",pos = vector(self.posAriMed[1][0],self.posAriMed[1][1],self.posAriMed[1][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="2",pos = vector(self.posAriMed[2][0],self.posAriMed[2][1],self.posAriMed[2][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="3",pos = vector(self.posAriMed[3][0],self.posAriMed[3][1],self.posAriMed[3][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="4",pos = vector(self.posAriMed[4][0],self.posAriMed[4][1],self.posAriMed[4][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="5",pos = vector(self.posAriMed[5][0],self.posAriMed[5][1],self.posAriMed[5][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="6",pos = vector(self.posAriMed[6][0],self.posAriMed[6][1],self.posAriMed[6][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="7",pos = vector(self.posAriMed[7][0],self.posAriMed[7][1],self.posAriMed[7][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="8",pos = vector(self.posAriMed[8][0],self.posAriMed[8][1],self.posAriMed[8][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="9",pos = vector(self.posAriMed[9][0],self.posAriMed[9][1],self.posAriMed[9][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="10",pos = vector(self.posAriMed[10][0],self.posAriMed[10][1],self.posAriMed[10][2]),color=color.red, height=0.2 , billboard=True),
                                    text(text ="11",pos = vector(self.posAriMed[11][0],self.posAriMed[11][1],self.posAriMed[11][2]),color=color.red, height=0.2 , billboard=True)])
        
        self.posCaraMed = np.array([f.punMedioCaraParticula(0, self.vertices, self.carasVertices, len(self.caras[0])),
                                   f.punMedioCaraParticula(1, self.vertices, self.carasVertices, len(self.caras[1])),
                                   f.punMedioCaraParticula(2, self.vertices, self.carasVertices, len(self.caras[2])),
                                   f.punMedioCaraParticula(3, self.vertices, self.carasVertices, len(self.caras[3])),
                                   f.punMedioCaraParticula(4, self.vertices, self.carasVertices, len(self.caras[4])),
                                   f.punMedioCaraParticula(5, self.vertices, self.carasVertices, len(self.caras[5]))])
        
        self.posCaraPlano = self.posCaraMed
        
        #Identificamos las caras en la particula
        self.numCaras = np.array([text(text ="0",pos = vector(self.posCaraMed[0][0], self.posCaraMed[0][1] + 0.1, self.posCaraMed[0][2]),color=color.white, height=0.2 , billboard=True),
                                  text(text ="1",pos = vector(self.posCaraMed[1][0], self.posCaraMed[1][1] + 0.1, self.posCaraMed[1][2]),color=color.white, height=0.2 , billboard=True),
                                  text(text ="2",pos = vector(self.posCaraMed[2][0], self.posCaraMed[2][1] + 0.1, self.posCaraMed[2][2]),color=color.white, height=0.2 , billboard=True),
                                  text(text ="3",pos = vector(self.posCaraMed[3][0], self.posCaraMed[3][1] + 0.1, self.posCaraMed[3][2]),color=color.white, height=0.2 , billboard=True),
                                  text(text ="4",pos = vector(self.posCaraMed[4][0], self.posCaraMed[4][1] + 0.1, self.posCaraMed[4][2]),color=color.white, height=0.2 , billboard=True),
                                  text(text ="5",pos = vector(self.posCaraMed[5][0], self.posCaraMed[5][1] + 0.1, self.posCaraMed[5][2]),color=color.white, height=0.2 , billboard=True)])
    
    
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
        self.posCaraPlano = self.posCaraMed