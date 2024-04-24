from vpython import *
import random as ran
import numpy as np
import math as ma


scene.title = "Pruebas 2 de SLM, por Jaime Velásquez\n"

poX = arrow(pos = vector(0,0,0), axis = vector(5,0,0), color = color.green, shaftwidth = 0.1)
tx = text(text ="X",pos = poX.axis,color=color.green, height=0.4 , billboard=True)
poY = arrow(pos = vector(0,0,0), axis = vector(0,5,0), color = color.yellow, shaftwidth = 0.1)
tx = text(text ="Y",pos = poY.axis,color=color.yellow, height=0.4 , billboard=True)
poZ = arrow(pos = vector(0,0,0), axis = vector(0,0,5), color = color.magenta, shaftwidth = 0.1)
tx = text(text ="Z",pos = poZ.axis,color=color.magenta, height=0.4 , billboard=True)
#Generamos los ejes x, y, z
poXne = arrow(pos = vector(0,0,0), axis = vector(-5,0,0), color = color.green, shaftwidth = 0.1, opacity = 0.1)
poYne = arrow(pos = vector(0,0,0), axis = vector(0,-5,0), color = color.yellow, shaftwidth = 0.1, opacity = 0.1)
poZne = arrow(pos = vector(0,0,0), axis = vector(0,0,-5), color = color.magenta, shaftwidth = 0.1, opacity = 0.1)
#Generamos los ejes negativos de x, y, z


def proyeccion(pun, dNormal, d):#se ingresa un punto y se devuelve su proyeccion en el plano
    lamb = -1*((dNormal[0]*pun[0] + dNormal[1]*pun[1] + dNormal[2]*pun[2] + d) / (np.power(dNormal[0],2) + np.power(dNormal[1],2) + np.power(dNormal[2],2)))
    #lambda para la proyeccion de un punto en el plano
    
    punPlano = [pun[0] + lamb*dNormal[0], pun[1] + lamb*dNormal[1], pun[2] + lamb*dNormal[2]]
    #punto en el plano
    return punPlano

def distancia(pun1,pun2):#distancia entre 2 puntos
    dis = np.sqrt(np.power(pun1[0]-pun2[0],2) + np.power(pun1[1]-pun2[1],2) + np.power(pun1[2]-pun2[2],2))
    return dis

def punAleaAris(ari,t):#generamos un punto aleatorio en una arista
    deltaP = [ari[1][0] - ari[0][0], ari[1][1] - ari[0][1], ari[1][2] - ari[0][2]]
    P = [ari[0][0] + t * deltaP[0], ari[0][1] + t * deltaP[1], ari[0][2] + t * deltaP[2]]
    return P

#lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

def proyecRPlano(puntoPlano, puntoRef, puntoAProyectar):
    dis = [puntoRef[0] - puntoPlano[0], puntoRef[1] - puntoPlano[1], puntoRef[2] - puntoPlano[2]]
    #es el vector distancia entre el plano y el centroide B

    moPlano = np.sqrt(np.power(dis[0],2) + np.power(dis[1],2) + np.power(dis[2],2))
    #calculamos el modulo de un vector del plano

    dNormal = [dis[0]/moPlano, dis[1]/moPlano, dis[2]/moPlano]
    #vector normal del plano al centroide B

    d = (dNormal[0]*puntoPlano[0] + dNormal[1]*puntoPlano[1] + dNormal[2]*puntoPlano[2]) * -1
    #calculamos d en base a la ecuacion del plano

    puntoProyectado = proyeccion(puntoAProyectar, dNormal, d)
    return puntoProyectado

def calculoT(pun, ari):
    t = (((pun[0]-ari[0][0])+(pun[1]-ari[0][1])+(pun[2]-ari[0][2]))/((ari[1][0]-ari[0][0])+(ari[1][1]-ari[0][1])+(ari[1][2]-ari[0][2])))
    return t

def punMedioCara(cara):#buscamos el punto medio de un cara
    
    suma = Va[carasVertices[cara][0]]
    
    for i in range(1,len(caras[cara])):
        suma = suma + Va[carasVertices[cara][i]]
    
    PaFi = suma / len(carasVertices[cara])
    
    '''
    ta = 0.5#punto medio
    
    ari1 = np.array([Va[aristas[caras[cara][1]][0]],Va[aristas[caras[cara][1]][1]]])
    ari2 = np.array([Va[aristas[caras[cara][3]][0]],Va[aristas[caras[cara][3]][1]]])
    #Generamos las 2 aristas paralelas
    
    Pa1 = punAleaAris(ari1,ta)
    Pa2 = punAleaAris(ari2,ta)
    ariNuevo = np.array([Pa1,Pa2])
    #Generamos una nueva "arista" con los puntos generados aleatoriamente
    
    PaFi = punAleaAris(ariNuevo,ta)
    '''
    return PaFi

def dentro(P,car):#entra un punto y una cara para ver si el punto esta dentro de ella
    suma = 0
    
    for i in range(len(caras[car])):
        ve1 = Va[aristas[caras[car][i]][0]]
        ve2 = Va[aristas[caras[car][i]][1]]
        vector1 = np.array([ve1[0]-P[0],ve1[1]-P[1],ve1[2]-P[2]])
        vector2 = np.array([ve2[0]-P[0],ve2[1]-P[1],ve2[2]-P[2]])
        
        top = vector1[0]*vector2[0] + vector1[1]*vector2[1] + vector1[2]*vector2[2]
        bot1 = np.sqrt((vector1[0]**2) + (vector1[1]**2) + (vector1[2]**2))
        bot2 = np.sqrt((vector2[0]**2) + (vector2[1]**2) + (vector2[2]**2))

        angu = ma.degrees(np.arccos(top/(bot1*bot2)))
        suma = angu + suma
        
    if suma > 359 and suma < 361:
        estaDentro = 1
    else:
        estaDentro = 0
    
    return estaDentro

def zonaCritica(ari1, ari2, punto):#entran las 2 aristas y un punto en el espacio
    
    vector1 = np.array([ari1[0]-ari2[0],ari1[1]-ari2[1],ari1[2]-ari2[2]])
    vector2 = np.array([ari1[0]-punto[0],ari1[1]-punto[1],ari1[2]-punto[2]])
        
    top = vector1[0]*vector2[0] + vector1[1]*vector2[1] + vector1[2]*vector2[2]
    bot1 = np.sqrt((vector1[0]**2) + (vector1[1]**2) + (vector1[2]**2))
    bot2 = np.sqrt((vector2[0]**2) + (vector2[1]**2) + (vector2[2]**2))
    
    #print("bot1 y bot2: ",bot1,bot2,"\n\n\n\n\n\n")
    
    if bot1 == 0.0:
        bot1 = 0.01
        
    if bot2 == 0.0:
        bot2 = 0.01
    
    angu = ma.degrees(np.arccos(top/(bot1*bot2)))
    
    return angu

def menorVertice(punto):
    vertMenor = [Va[len(Va)-1],Va[len(Va)-2]]
    disMenor = [distancia(vertMenor[0], punto), distancia(vertMenor[1], punto)]
    
    print("vertMenor: ", vertMenor)
    print("disMenor: ", disMenor)
    print("\n")
    for i in range(len(Va)-2):
        vertAux = Va[i]
        disAux = distancia(vertAux, punto)
        print(vertAux)
        print(disAux,"\n")
        if disAux < disMenor[0] and disMenor[0] >= disMenor[1]:
            disMenor[0] = disAux
            vertMenor[0] = vertAux
        elif disAux < disMenor[1] and disMenor[1] >= disMenor[0]:
            disMenor[1] = disAux
            vertMenor[1] = vertAux
    return vertMenor

def SL(centroide, punto):
    
    carasDistanciaMenor = np.array([len(caras)-1,len(caras)-2])
    distanciasCara = np.array([distancia(punMedioCara(len(caras)-1),punto),distancia(punMedioCara(len(caras)-2),punto)])
    
    '''
    print("\n\n\n\n\n","carasDistanciaMenor",carasDistanciaMenor)
    print("distnaciasCara",distanciasCara,"\n\n\n\n\n")
    '''
    
    for i in range(len(caras)-2):
        disAux = distancia(punMedioCara(i), punto)
        #print(disAux)
        if disAux < distanciasCara[0] and distanciasCara[0] >= distanciasCara[1]:
            distanciasCara[0] = disAux
            carasDistanciaMenor[0] = i
        elif disAux < distanciasCara[1] and distanciasCara[1] >= distanciasCara[0]:
            distanciasCara[1] = disAux
            carasDistanciaMenor[1] = i
    '''
    print("\n\n\n\n\n","carasDistanciaMenor",carasDistanciaMenor)
    print("distanciasCara",distanciasCara,"\n\n\n\n\n")
    '''
    if distanciasCara[0] > distanciasCara[1]:
        caraDistanciaMenor = carasDistanciaMenor[1]
        caraDistanciaMenor2 = carasDistanciaMenor[0]
    else:
        caraDistanciaMenor = carasDistanciaMenor[0]
        caraDistanciaMenor2 = carasDistanciaMenor[1]
    
    punMedio = punMedioCara(caraDistanciaMenor)#punto medio de la cara
    
    puntoProyectado = proyecRPlano(punMedio, centroide, punto)
    #SLpunto = sphere(pos = vector(puntoProyectado[0],puntoProyectado[1],puntoProyectado[2]), color = color.green, radius = 0.1)
    estaDentro = dentro(puntoProyectado, caraDistanciaMenor)
    
    print("\n\n------------")
    print("carasDistanciaMenor: ",caraDistanciaMenor)
    print("------------\n\n")
    
    if estaDentro == 1:
        Pn = puntoProyectado
    else:
        vertMenor = menorVertice(punto)
        
        print("\n\n------------")
        print("vertMenor: ",vertMenor)
        print("------------\n\n")
        
        angu1 = zonaCritica(vertMenor[0], vertMenor[1], punto)
        angu2 = zonaCritica(vertMenor[1], vertMenor[0], punto)
        '''
        print("\n\n------------")
        print("angu1 y angu2: ",angu1,angu2)
        print("------------\n\n")
        '''
        if angu1 >= 90 or angu2 >= 90:
            
            if distancia(vertMenor[0], punto) < distancia(vertMenor[1], punto):
                Pn = vertMenor[0]
            else:
                Pn = vertMenor[1]
        else:
            vectorAB = np.array([vertMenor[1][0]-vertMenor[0][0],vertMenor[1][1]-vertMenor[0][1],vertMenor[1][2]-vertMenor[0][2]])
            vectorAP = np.array([punto[0] - vertMenor[0][0],punto[1] - vertMenor[0][1],punto[2] - vertMenor[0][2]])
            Pn = vertMenor[0] + (np.dot(vectorAP,vectorAB) / np.dot(vectorAB,vectorAB)) * vectorAB
            '''
            punMedio = punMedioCara(caraDistanciaMenor2)#punto medio de la cara
            puntoProyectado = proyecRPlano(punMedio, centroide, puntoProyectado)
            Pn = puntoProyectado
            '''
    return Pn

def inicio():
    global Va, Vb, caras, aristas, carasVertices
    posA = np.array([ran.uniform(-5, 5),ran.uniform(-5, 5),ran.uniform(-5, 5)])
    #posA = np.array([1.5,-1.5,-2])
    #posicion del centroide A
    #Vcc = 0
    #Vcc corresponde a la distancia entre ambos centroides
    '''
    while 1:#ciclo se ejecuta hasta que la distancia entre el
                    #centroide A y B sea mayor a 5
        posB = np.array([ran.uniform(-5, 5),ran.uniform(-5, 5),ran.uniform(-5, 5)])
        #generamos un punto aleatorio B
        Vcc = distancia(posA,posB)
        if Vcc > 3 and Vcc < 3.5:
            break
    print(posB)
    '''
    posB = np.array([0,0.8,2])
    #posB = np.array([-1,1,1])
    cParA = sphere(pos = vector(posA[0],posA[1],posA[2]), color = color.green, radius = 0.1)
    #mostramos centroide para la particula A
    cParB = sphere(pos = vector(posB[0],posB[1],posB[2]), color = color.red, radius = 0.1)
    #mostramos centroide para la particula B
    VCC = arrow(pos = cParA.pos, axis = cParB.pos - cParA.pos, color = color.orange, shaftwidth = 0.05)
    #VCC corresponde al vector de centroide a centroide
    
    
    #inicio cubo
    #Cubo
    posVert = np.array([[1,1,1],
                        [1,1,-1],
                        [1,-1,-1],
                        [1,-1,1],
                        [-1,-1,-1],
                        [-1,-1,1],
                        [-1,1,1],
                        [-1,1,-1]])
    #posicion de los vertices globales con respecto al centroide
    
    aristas = np.array([[0,1],#arista 0
                        [1,2],#arista 1
                        [2,3],#arista 2
                        [3,0],#arista 3
                        [1,7],#arista 4
                        [4,7],#arista 5
                        [4,2],#arista 6
                        [7,6],#arista 7
                        [6,5],#arista 8
                        [5,4],#arista 9
                        [6,0],#arista 10
                        [3,5]])#arista 11
    #aristas particula B y A
    
    carasVertices = np.array([[0,1,2,3],     #cara 0
                              [1,7,4,2],     #cara 1
                              [7,6,5,4],     #cara 2
                              [6,0,3,5],     #cara 3
                              [5,4,2,3],     #cara 4
                              [7,6,0,1]])    #cara 5
    
    caras = np.array([[0,1,2,3],   #cara 0
                      [4,5,6,1],   #cara 1
                      [7,8,9,5],   #cara 2
                      [10,3,11,8], #cara 3
                      [9,11,2,6],  #cara 4
                      [7,4,0,10]]) #cara 5
    
    Va = np.array([[posA[0]+posVert[0][0],posA[1]+posVert[0][1],posA[2]+posVert[0][2]],
                   [posA[0]+posVert[1][0],posA[1]+posVert[1][1],posA[2]+posVert[1][2]],
                   [posA[0]+posVert[2][0],posA[1]+posVert[2][1],posA[2]+posVert[2][2]],
                   [posA[0]+posVert[3][0],posA[1]+posVert[3][1],posA[2]+posVert[3][2]],
                   [posA[0]+posVert[4][0],posA[1]+posVert[4][1],posA[2]+posVert[4][2]],
                   [posA[0]+posVert[5][0],posA[1]+posVert[5][1],posA[2]+posVert[5][2]],
                   [posA[0]+posVert[6][0],posA[1]+posVert[6][1],posA[2]+posVert[6][2]],
                   [posA[0]+posVert[7][0],posA[1]+posVert[7][1],posA[2]+posVert[7][2]]])
    #Generamos los vetices en base a nuestro centroide de la prticula A
    
    verticesA = [sphere(pos = vector(Va[0][0],Va[0][1],Va[0][2]), color = color.purple, radius = 0.1),
                 sphere(pos = vector(Va[1][0],Va[1][1],Va[1][2]), color = color.red, radius = 0.1),
                 sphere(pos = vector(Va[2][0],Va[2][1],Va[2][2]), color = color.blue, radius = 0.1),
                 sphere(pos = vector(Va[3][0],Va[3][1],Va[3][2]), color = color.yellow, radius = 0.1),
                 sphere(pos = vector(Va[4][0],Va[4][1],Va[4][2]), color = color.green, radius = 0.1),
                 sphere(pos = vector(Va[5][0],Va[5][1],Va[5][2]), color = color.cyan, radius = 0.1),
                 sphere(pos = vector(Va[6][0],Va[6][1],Va[6][2]), color = color.magenta, radius = 0.1),
                 sphere(pos = vector(Va[7][0],Va[7][1],Va[7][2]), color = color.white, radius = 0.1)]
    #vertices de la particula A mostrados por pantalla
    
    aristasA = [arrow(pos = vector(Va[aristas[0][0]][0],Va[aristas[0][0]][1],Va[aristas[0][0]][2]), axis = vector(Va[aristas[0][1]][0],Va[aristas[0][1]][1],Va[aristas[0][1]][2]) - vector(Va[aristas[0][0]][0],Va[aristas[0][0]][1],Va[aristas[0][0]][2]), color = color.magenta, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[1][0]][0],Va[aristas[1][0]][1],Va[aristas[1][0]][2]), axis = vector(Va[aristas[1][1]][0],Va[aristas[1][1]][1],Va[aristas[1][1]][2]) - vector(Va[aristas[1][0]][0],Va[aristas[1][0]][1],Va[aristas[1][0]][2]), color = color.purple, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[2][0]][0],Va[aristas[2][0]][1],Va[aristas[2][0]][2]), axis = vector(Va[aristas[2][1]][0],Va[aristas[2][1]][1],Va[aristas[2][1]][2]) - vector(Va[aristas[2][0]][0],Va[aristas[2][0]][1],Va[aristas[2][0]][2]), color = color.yellow, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[3][0]][0],Va[aristas[3][0]][1],Va[aristas[3][0]][2]), axis = vector(Va[aristas[3][1]][0],Va[aristas[3][1]][1],Va[aristas[3][1]][2]) - vector(Va[aristas[3][0]][0],Va[aristas[3][0]][1],Va[aristas[3][0]][2]), color = color.blue, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[4][0]][0],Va[aristas[4][0]][1],Va[aristas[4][0]][2]), axis = vector(Va[aristas[4][1]][0],Va[aristas[4][1]][1],Va[aristas[4][1]][2]) - vector(Va[aristas[4][0]][0],Va[aristas[4][0]][1],Va[aristas[4][0]][2]), color = color.green, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[5][0]][0],Va[aristas[5][0]][1],Va[aristas[5][0]][2]), axis = vector(Va[aristas[5][1]][0],Va[aristas[5][1]][1],Va[aristas[5][1]][2]) - vector(Va[aristas[5][0]][0],Va[aristas[5][0]][1],Va[aristas[5][0]][2]), color = color.orange, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[6][0]][0],Va[aristas[6][0]][1],Va[aristas[6][0]][2]), axis = vector(Va[aristas[6][1]][0],Va[aristas[6][1]][1],Va[aristas[6][1]][2]) - vector(Va[aristas[6][0]][0],Va[aristas[6][0]][1],Va[aristas[6][0]][2]), color = color.red, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[7][0]][0],Va[aristas[7][0]][1],Va[aristas[7][0]][2]), axis = vector(Va[aristas[7][1]][0],Va[aristas[7][1]][1],Va[aristas[7][1]][2]) - vector(Va[aristas[7][0]][0],Va[aristas[7][0]][1],Va[aristas[7][0]][2]), color = color.white, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[8][0]][0],Va[aristas[8][0]][1],Va[aristas[8][0]][2]), axis = vector(Va[aristas[8][1]][0],Va[aristas[8][1]][1],Va[aristas[8][1]][2]) - vector(Va[aristas[8][0]][0],Va[aristas[8][0]][1],Va[aristas[8][0]][2]), color = color.cyan, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[9][0]][0],Va[aristas[9][0]][1],Va[aristas[9][0]][2]), axis = vector(Va[aristas[9][1]][0],Va[aristas[9][1]][1],Va[aristas[9][1]][2]) - vector(Va[aristas[9][0]][0],Va[aristas[9][0]][1],Va[aristas[9][0]][2]), color = color.blue, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[10][0]][0],Va[aristas[10][0]][1],Va[aristas[10][0]][2]), axis = vector(Va[aristas[10][1]][0],Va[aristas[10][1]][1],Va[aristas[10][1]][2]) - vector(Va[aristas[10][0]][0],Va[aristas[10][0]][1],Va[aristas[10][0]][2]), color = color.green, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[11][0]][0],Va[aristas[11][0]][1],Va[aristas[11][0]][2]), axis = vector(Va[aristas[11][1]][0],Va[aristas[11][1]][1],Va[aristas[11][1]][2]) - vector(Va[aristas[11][0]][0],Va[aristas[11][0]][1],Va[aristas[11][0]][2]), color = color.orange, shaftwidth = 0.05)]
    #aristas de la particula A mostradas por pantalla
    
    
    #Identificamos los vertices en la particula
    v1 = text(text ="0",pos = vector(Va[0][0],Va[0][1]+0.1,Va[0][2]),color=color.green, height=0.2 , billboard=True)
    v2 = text(text ="1",pos = vector(Va[1][0],Va[1][1]+0.1,Va[1][2]),color=color.green, height=0.2 , billboard=True)
    v3 = text(text ="2",pos = vector(Va[2][0],Va[2][1]-0.2,Va[2][2]),color=color.green, height=0.2 , billboard=True)
    v4 = text(text ="3",pos = vector(Va[3][0],Va[3][1]-0.2,Va[3][2]),color=color.green, height=0.2 , billboard=True)
    v5 = text(text ="4",pos = vector(Va[4][0],Va[4][1]-0.2,Va[4][2]),color=color.green, height=0.2 , billboard=True)
    v6 = text(text ="5",pos = vector(Va[5][0],Va[5][1]-0.2,Va[5][2]),color=color.green, height=0.2 , billboard=True)
    v7 = text(text ="6",pos = vector(Va[6][0],Va[6][1]+0.1,Va[6][2]),color=color.green, height=0.2 , billboard=True)
    v8 = text(text ="7",pos = vector(Va[7][0],Va[7][1]+0.1,Va[7][2]),color=color.green, height=0.2 , billboard=True)
    '''
    '''
    #Identificamos las aristas en la particula
    a1m = punAleaAris(np.array([Va[aristas[0][0]],Va[aristas[0][1]]]),0.5)
    a1 = text(text ="0",pos = vector(a1m[0],a1m[1],a1m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a2m = punAleaAris(np.array([Va[aristas[1][0]],Va[aristas[1][1]]]),0.5)
    a2 = text(text ="1",pos = vector(a2m[0],a2m[1],a2m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a3m = punAleaAris(np.array([Va[aristas[2][0]],Va[aristas[2][1]]]),0.5)
    a3 = text(text ="2",pos = vector(a3m[0],a3m[1],a3m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a4m = punAleaAris(np.array([Va[aristas[3][0]],Va[aristas[3][1]]]),0.5)
    a4 = text(text ="3",pos = vector(a4m[0],a4m[1],a4m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a5m = punAleaAris(np.array([Va[aristas[4][0]],Va[aristas[4][1]]]),0.5)
    a5 = text(text ="4",pos = vector(a5m[0],a5m[1],a5m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a6m = punAleaAris(np.array([Va[aristas[5][0]],Va[aristas[5][1]]]),0.5)
    a6 = text(text ="5",pos = vector(a6m[0],a6m[1],a6m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a7m = punAleaAris(np.array([Va[aristas[6][0]],Va[aristas[6][1]]]),0.5)
    a7 = text(text ="6",pos = vector(a7m[0],a7m[1],a7m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a8m = punAleaAris(np.array([Va[aristas[7][0]],Va[aristas[7][1]]]),0.5)
    a8 = text(text ="7",pos = vector(a8m[0],a8m[1],a8m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a9m = punAleaAris(np.array([Va[aristas[8][0]],Va[aristas[8][1]]]),0.5)
    a9 = text(text ="8",pos = vector(a9m[0],a9m[1],a9m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a10m = punAleaAris(np.array([Va[aristas[9][0]],Va[aristas[9][1]]]),0.5)
    a10 = text(text ="9",pos = vector(a10m[0],a10m[1],a10m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a11m = punAleaAris(np.array([Va[aristas[10][0]],Va[aristas[10][1]]]),0.5)
    a11 = text(text ="10",pos = vector(a11m[0],a11m[1],a11m[2]),color=color.orange, height=0.2 , billboard=True)
    
    a12m = punAleaAris(np.array([Va[aristas[11][0]],Va[aristas[11][1]]]),0.5)
    a12 = text(text ="11",pos = vector(a12m[0],a12m[1],a12m[2]),color=color.orange, height=0.2 , billboard=True)
    
    
    #Identificamos las caras en la particula
    
    PaFinal = punMedioCara(0)
    #Generamos un punto aleatorio en la nueva cara
    c1 = text(text ="0",pos = vector(PaFinal[0],PaFinal[1]+0.1,PaFinal[2]),color=color.white, height=0.2 , billboard=True)
    
    PaFinal = punMedioCara(1)
    #Generamos un punto aleatorio en la nueva cara
    c2 = text(text ="1",pos = vector(PaFinal[0],PaFinal[1]+0.1,PaFinal[2]),color=color.white, height=0.2 , billboard=True)
    
    PaFinal = punMedioCara(2)
    #Generamos un punto aleatorio en la nueva cara
    c3 = text(text ="2",pos = vector(PaFinal[0],PaFinal[1]+0.1,PaFinal[2]),color=color.white, height=0.2 , billboard=True)
    
    PaFinal = punMedioCara(3)
    #Generamos un punto aleatorio en la nueva cara
    c4 = text(text ="3",pos = vector(PaFinal[0],PaFinal[1]+0.1,PaFinal[2]),color=color.white, height=0.2 , billboard=True)
    
    PaFinal = punMedioCara(4)
    #Generamos un punto aleatorio en la nueva cara
    c5 = text(text ="4",pos = vector(PaFinal[0]+0.1,PaFinal[1],PaFinal[2]),color=color.white, height=0.2 , billboard=True)
    
    PaFinal = punMedioCara(5)
    c6 = text(text ="5",pos = vector(PaFinal[0]+0.1,PaFinal[1],PaFinal[2]),color=color.white, height=0.2 , billboard=True)
    
    #fin cubo
    
    
    '''
    
    #creamos la primer area de conflicto
    ac1X = arrow(pos = vector(Va[0][0],Va[0][1],Va[0][2]), axis = vector(Va[0][0]+2,Va[0][1],Va[0][2]) - vector(Va[0][0],Va[0][1],Va[0][2]), color = color.green, shaftwidth = 0.1)
    ac1tx1 = text(text = str(int(Va[0][0]+1)),pos = vector(Va[0][0]+1,Va[0][1]+0.1,Va[0][2]),color=color.magenta, height=0.2 , billboard=True)
    ac1tx2 = text(text = str(int(Va[0][0]+2)),pos = vector(Va[0][0]+2,Va[0][1]+0.1,Va[0][2]),color=color.magenta, height=0.2 , billboard=True)
    
    ac1Y = arrow(pos = vector(Va[0][0],Va[0][1],Va[0][2]), axis = vector(Va[0][0],Va[0][1]+2,Va[0][2]) - vector(Va[0][0],Va[0][1],Va[0][2]), color = color.yellow, shaftwidth = 0.1)
    ac1tx3 = text(text = str(int(Va[0][1]+1)),pos = vector(Va[0][0]+0.1,Va[0][1]+1,Va[0][2]),color=color.magenta, height=0.2 , billboard=True)
    ac1tx4 = text(text = str(int(Va[0][1]+2)),pos = vector(Va[0][0]+0.1,Va[0][1]+2,Va[0][2]),color=color.magenta, height=0.2 , billboard=True)
    
    ac1Z = arrow(pos = vector(Va[0][0],Va[0][1],Va[0][2]), axis = vector(Va[0][0],Va[0][1],Va[0][2]+2) - vector(Va[0][0],Va[0][1],Va[0][2]), color = color.cyan, shaftwidth = 0.1)
    ac1tx5 = text(text = str(int(Va[0][2]+1)),pos = vector(Va[0][0]+0.1,Va[0][1],Va[0][2]+1),color=color.magenta, height=0.2 , billboard=True)
    ac1tx6 = text(text = str(int(Va[0][2]+2)),pos = vector(Va[0][0]+0.1,Va[0][1],Va[0][2]+2),color=color.magenta, height=0.2 , billboard=True)
    
    
    ac1 = box(pos = vector(Va[0][0]+1,Va[0][1]+1,Va[0][2]+1), size = vector(2,2,2), opacity = 0.5, color = color.cyan)
    
    #creamos la segunda area de conflicto
    ac2X = arrow(pos = vector(Va[1][0],Va[1][1],Va[1][2]), axis = vector(Va[1][0]+2,Va[1][1],Va[1][2]) - vector(Va[1][0],Va[1][1],Va[1][2]), color = color.green, shaftwidth = 0.1)
    ac2tx1 = text(text = str(int(Va[1][0]+1)),pos = vector(Va[1][0]+1,Va[1][1]+0.1,Va[1][2]),color=color.magenta, height=0.2 , billboard=True)
    ac2tx2 = text(text = str(int(Va[1][0]+2)),pos = vector(Va[1][0]+2,Va[1][1]+0.1,Va[1][2]),color=color.magenta, height=0.2 , billboard=True)
    
    ac2Y = arrow(pos = vector(Va[1][0],Va[1][1],Va[1][2]), axis = vector(Va[1][0],Va[1][1]+2,Va[1][2]) - vector(Va[1][0],Va[1][1],Va[1][2]), color = color.yellow, shaftwidth = 0.1)
    ac2tx3 = text(text = str(int(Va[1][1]+1)),pos = vector(Va[1][0]+0.1,Va[1][1]+1,Va[1][2]),color=color.magenta, height=0.2 , billboard=True)
    ac2tx4 = text(text = str(int(Va[1][1]+2)),pos = vector(Va[1][0]+0.1,Va[1][1]+2,Va[1][2]),color=color.magenta, height=0.2 , billboard=True)
    
    ac2Z = arrow(pos = vector(Va[0][0]+2,Va[0][1],Va[0][2]), axis = vector(Va[1][0]+2,Va[1][1],Va[1][2]) - vector(Va[0][0]+2,Va[0][1],Va[0][2]), color = color.cyan, shaftwidth = 0.1)
    ac2tx5 = text(text = "0",pos = vector(3,1,0),color=color.magenta, height=0.2 , billboard=True)
    
    
    ac2 = box(pos = vector(Va[1][0]+1,Va[1][1]+1,Va[1][2]+1), size = vector(2,2,2), opacity = 0.5, color = color.red)
    '''
    
    #inicio tetaedro
    '''#Tetraedro
    posVert = np.array([[1,1,1],
                        [-1,-1,1],
                        [-1,1,-1],
                        [1,-1,-1]])
    #posicion de los vertices globales con respecto al centroide
    print(distancia(posVert[2],posVert[1]))
    Va = np.array([[posA[0]+posVert[0][0],posA[1]+posVert[0][1],posA[2]+posVert[0][2]],
                   [posA[0]+posVert[1][0],posA[1]+posVert[1][1],posA[2]+posVert[1][2]],
                   [posA[0]+posVert[2][0],posA[1]+posVert[2][1],posA[2]+posVert[2][2]],
                   [posA[0]+posVert[3][0],posA[1]+posVert[3][1],posA[2]+posVert[3][2]]])
    #Generamos los vetices en base a nuestro centroide de la particula A
    
    aristas = np.array([[0,1],#arista 0
                        [1,2],#arista 1
                        [2,0],#arista 2
                        [3,1],#arista 3
                        [0,3],#arista 4
                        [3,2]]#arista 5
                        )
    #aristas particula B y A
    carasVertices = np.array([[0,1,2],
                              [1,2,3],
                              [2,3,0],
                              [0,3,1]])
    
    caras = np.array([[0,1,2],   #cara 0
                      [1,3,2],   #cara 1
                      [2,5,4],   #cara 2
                      [0,4,3]])  #cara 3
    
    verticesA = [sphere(pos = vector(Va[0][0],Va[0][1],Va[0][2]), color = color.purple, radius = 0.1),
                 sphere(pos = vector(Va[1][0],Va[1][1],Va[1][2]), color = color.red, radius = 0.1),
                 sphere(pos = vector(Va[2][0],Va[2][1],Va[2][2]), color = color.blue, radius = 0.1),
                 sphere(pos = vector(Va[3][0],Va[3][1],Va[3][2]), color = color.yellow, radius = 0.1)]
    #vertices de la particula A mostrados por pantalla
    
    aristasA = [arrow(pos = vector(Va[aristas[0][0]][0],Va[aristas[0][0]][1],Va[aristas[0][0]][2]), axis = vector(Va[aristas[0][1]][0],Va[aristas[0][1]][1],Va[aristas[0][1]][2]) - vector(Va[aristas[0][0]][0],Va[aristas[0][0]][1],Va[aristas[0][0]][2]), color = color.red, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[1][0]][0],Va[aristas[1][0]][1],Va[aristas[1][0]][2]), axis = vector(Va[aristas[1][1]][0],Va[aristas[1][1]][1],Va[aristas[1][1]][2]) - vector(Va[aristas[1][0]][0],Va[aristas[1][0]][1],Va[aristas[1][0]][2]), color = color.purple, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[2][0]][0],Va[aristas[2][0]][1],Va[aristas[2][0]][2]), axis = vector(Va[aristas[2][1]][0],Va[aristas[2][1]][1],Va[aristas[2][1]][2]) - vector(Va[aristas[2][0]][0],Va[aristas[2][0]][1],Va[aristas[2][0]][2]), color = color.yellow, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[3][0]][0],Va[aristas[3][0]][1],Va[aristas[3][0]][2]), axis = vector(Va[aristas[3][1]][0],Va[aristas[3][1]][1],Va[aristas[3][1]][2]) - vector(Va[aristas[3][0]][0],Va[aristas[3][0]][1],Va[aristas[3][0]][2]), color = color.blue, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[4][0]][0],Va[aristas[4][0]][1],Va[aristas[4][0]][2]), axis = vector(Va[aristas[4][1]][0],Va[aristas[4][1]][1],Va[aristas[4][1]][2]) - vector(Va[aristas[4][0]][0],Va[aristas[4][0]][1],Va[aristas[4][0]][2]), color = color.green, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[5][0]][0],Va[aristas[5][0]][1],Va[aristas[5][0]][2]), axis = vector(Va[aristas[5][1]][0],Va[aristas[5][1]][1],Va[aristas[5][1]][2]) - vector(Va[aristas[5][0]][0],Va[aristas[5][0]][1],Va[aristas[5][0]][2]), color = color.orange, shaftwidth = 0.05)]
    #aristas de la particula A mostradas por pantalla
    
    cara1 = punMedioCara(0)
    c1 = text(text ="0",pos = vector(cara1[0],cara1[1],cara1[2]),color=color.red, height=0.2 , billboard=True)
    
    cara2 = punMedioCara(1)
    c2 = text(text ="1",pos = vector(cara2[0],cara2[1],cara2[2]),color=color.red, height=0.2 , billboard=True)
    
    cara3 = punMedioCara(2)
    c3 = text(text ="2",pos = vector(cara3[0],cara3[1],cara3[2]),color=color.red, height=0.2 , billboard=True)
    
    cara4 = punMedioCara(3)
    c4 = text(text ="3",pos = vector(cara4[0],cara4[1],cara4[2]),color=color.red, height=0.2 , billboard=True)
    #mostramos por pantalla las caras
    '''
    
    #fin tetaedro
    
    '''
    #Identificamos los vertices en la particula
    v1 = text(text ="0",pos = vector(Va[0][0],Va[0][1]+0.1,Va[0][2]),color=color.green, height=0.2 , billboard=True)
    v2 = text(text ="1",pos = vector(Va[1][0],Va[1][1]+0.1,Va[1][2]),color=color.green, height=0.2 , billboard=True)
    v3 = text(text ="2",pos = vector(Va[2][0],Va[2][1]+0.1,Va[2][2]),color=color.green, height=0.2 , billboard=True)
    v4 = text(text ="3",pos = vector(Va[3][0],Va[3][1]+0.1,Va[3][2]),color=color.green, height=0.2 , billboard=True)
    '''
    '''
    #creamos la primer area de conflicto
    ac1X = arrow(pos = vector(Va[0][0],Va[0][1],Va[0][2]), axis = vector(2.70710678,1,2.70710678) - vector(Va[0][0],Va[0][1],Va[0][2]), color = color.green, shaftwidth = 0.1)
    
    ac1Y = arrow(pos = vector(Va[0][0],Va[0][1],Va[0][2]), axis = vector(2.41421356,2.41421356,1) - vector(Va[0][0],Va[0][1],Va[0][2]), color = color.yellow, shaftwidth = 0.1)
    
    ac1Z = arrow(pos = vector(Va[0][0],Va[0][1],Va[0][2]), axis = vector(1,2.41421356,2.41421356) - vector(Va[0][0],Va[0][1],Va[0][2]), color = color.cyan, shaftwidth = 0.1)
    
    
    ac2X = arrow(pos = vector(Va[2][0],Va[2][1],Va[2][2]), axis = vector(-2.41421356,2.41421356,-1) - vector(Va[2][0],Va[2][1],Va[2][2]), color = color.green, shaftwidth = 0.1)
    
    ac2Y = arrow(pos = vector(Va[2][0],Va[2][1],Va[2][2]), axis = vector(-1,2.41421356,-2.41421356) - vector(Va[2][0],Va[2][1],Va[2][2]), color = color.yellow, shaftwidth = 0.1)
    
    angu1 = arrow(pos = vector(Va[0][0],Va[0][1],Va[0][2]), axis = vector((-2.41421356-1)/2,(2.41421356+2.41421356)/2,(-1-2.41421356)/2) - vector(Va[0][0],Va[0][1],Va[0][2]), color = color.red, shaftwidth = 0.1)
    angu2 = arrow(pos = vector(Va[2][0],Va[2][1],Va[2][2]), axis = vector((-2.41421356-1)/2,(2.41421356+2.41421356)/2,(-1-2.41421356)/2) - vector(Va[2][0],Va[2][1],Va[2][2]), color = color.red, shaftwidth = 0.1)
    '''
    
    #inicio piramide
    '''#piramide
    #piramide = pyramid(pos = vector(0,-0.5,0), axis = vector(0,1,0), size = vector(2,2,2), opacity = 0.3)
    #centroide = sphere(pos = vector(0,0,0), color = color.purple, radius = 0.1)
    
    posVert = np.array([[1,-0.5,1],
                        [-1,-0.5,1],
                        [-1,-0.5,-1],
                        [1,-0.5,-1],
                        [0,1.5,0]])
    
    Va = np.array([[posA[0]+posVert[0][0],posA[1]+posVert[0][1],posA[2]+posVert[0][2]],
                   [posA[0]+posVert[1][0],posA[1]+posVert[1][1],posA[2]+posVert[1][2]],
                   [posA[0]+posVert[2][0],posA[1]+posVert[2][1],posA[2]+posVert[2][2]],
                   [posA[0]+posVert[3][0],posA[1]+posVert[3][1],posA[2]+posVert[3][2]],
                   [posA[0]+posVert[4][0],posA[1]+posVert[4][1],posA[2]+posVert[4][2]]])
    #Generamos los vetices en base a nuestro centroide de la prticula A
    
    aristas = np.array([[0,1],     #arista 0
                        [1,2],     #arista 1
                        [2,3],     #arista 2
                        [4,1],     #arista 3
                        [3,0],     #arista 4
                        [4,0],     #arista 5
                        [4,2],     #arista 6
                        [4,3]]     #arista 7
                        )
    #aristas particula A
    
    carasVertices = np.array([[3,0,1,2],
                              [4,0,3],
                              [4,3,2],
                              [4,1,2],
                              [4,1,0]])
    
    caras = np.array([[4,2,1,0],      #cara 0
                      [7,4,5],        #cara 1
                      [7,6,2],        #cara 2
                      [6,3,1],        #cara 3
                      [3,5,0]])       #cara 4
    
    verticesA = [sphere(pos = vector(Va[0][0],Va[0][1],Va[0][2]), color = color.purple, radius = 0.1),  #0
                 sphere(pos = vector(Va[1][0],Va[1][1],Va[1][2]), color = color.red, radius = 0.1),     #1
                 sphere(pos = vector(Va[2][0],Va[2][1],Va[2][2]), color = color.blue, radius = 0.1),    #2
                 sphere(pos = vector(Va[3][0],Va[3][1],Va[3][2]), color = color.yellow, radius = 0.1),  #3
                 sphere(pos = vector(Va[4][0],Va[4][1],Va[4][2]), color = color.green, radius = 0.1)]   #4
    #vertices de la particula A mostrados por pantalla
    
    aristasA = [arrow(pos = vector(Va[aristas[0][0]][0],Va[aristas[0][0]][1],Va[aristas[0][0]][2]), axis = vector(Va[aristas[0][1]][0],Va[aristas[0][1]][1],Va[aristas[0][1]][2]) - vector(Va[aristas[0][0]][0],Va[aristas[0][0]][1],Va[aristas[0][0]][2]), color = color.magenta, shaftwidth = 0.05), #0
                arrow(pos = vector(Va[aristas[1][0]][0],Va[aristas[1][0]][1],Va[aristas[1][0]][2]), axis = vector(Va[aristas[1][1]][0],Va[aristas[1][1]][1],Va[aristas[1][1]][2]) - vector(Va[aristas[1][0]][0],Va[aristas[1][0]][1],Va[aristas[1][0]][2]), color = color.purple, shaftwidth = 0.05),  #1
                arrow(pos = vector(Va[aristas[2][0]][0],Va[aristas[2][0]][1],Va[aristas[2][0]][2]), axis = vector(Va[aristas[2][1]][0],Va[aristas[2][1]][1],Va[aristas[2][1]][2]) - vector(Va[aristas[2][0]][0],Va[aristas[2][0]][1],Va[aristas[2][0]][2]), color = color.yellow, shaftwidth = 0.05),  #2
                arrow(pos = vector(Va[aristas[3][0]][0],Va[aristas[3][0]][1],Va[aristas[3][0]][2]), axis = vector(Va[aristas[3][1]][0],Va[aristas[3][1]][1],Va[aristas[3][1]][2]) - vector(Va[aristas[3][0]][0],Va[aristas[3][0]][1],Va[aristas[3][0]][2]), color = color.blue, shaftwidth = 0.05),    #3
                arrow(pos = vector(Va[aristas[4][0]][0],Va[aristas[4][0]][1],Va[aristas[4][0]][2]), axis = vector(Va[aristas[4][1]][0],Va[aristas[4][1]][1],Va[aristas[4][1]][2]) - vector(Va[aristas[4][0]][0],Va[aristas[4][0]][1],Va[aristas[4][0]][2]), color = color.green, shaftwidth = 0.05),   #4
                arrow(pos = vector(Va[aristas[5][0]][0],Va[aristas[5][0]][1],Va[aristas[5][0]][2]), axis = vector(Va[aristas[5][1]][0],Va[aristas[5][1]][1],Va[aristas[5][1]][2]) - vector(Va[aristas[5][0]][0],Va[aristas[5][0]][1],Va[aristas[5][0]][2]), color = color.orange, shaftwidth = 0.05),  #5
                arrow(pos = vector(Va[aristas[6][0]][0],Va[aristas[6][0]][1],Va[aristas[6][0]][2]), axis = vector(Va[aristas[6][1]][0],Va[aristas[6][1]][1],Va[aristas[6][1]][2]) - vector(Va[aristas[6][0]][0],Va[aristas[6][0]][1],Va[aristas[6][0]][2]), color = color.red, shaftwidth = 0.05),     #6
                arrow(pos = vector(Va[aristas[7][0]][0],Va[aristas[7][0]][1],Va[aristas[7][0]][2]), axis = vector(Va[aristas[7][1]][0],Va[aristas[7][1]][1],Va[aristas[7][1]][2]) - vector(Va[aristas[7][0]][0],Va[aristas[7][0]][1],Va[aristas[7][0]][2]), color = color.cyan, shaftwidth = 0.05)]    #7
    #aristas de la particula A mostradas por pantalla
    
    cara1 = punMedioCara(0)
    c1 = text(text ="0",pos = vector(cara1[0],cara1[1],cara1[2]),color=color.red, height=0.2 , billboard=True)
    
    cara2 = punMedioCara(1)
    c2 = text(text ="1",pos = vector(cara2[0],cara2[1],cara2[2]),color=color.red, height=0.2 , billboard=True)
    
    cara3 = punMedioCara(2)
    c3 = text(text ="2",pos = vector(cara3[0],cara3[1],cara3[2]),color=color.red, height=0.2 , billboard=True)
    
    cara4 = punMedioCara(3)
    c4 = text(text ="3",pos = vector(cara4[0],cara4[1],cara4[2]),color=color.red, height=0.2 , billboard=True)
    #mostramos por pantalla las caras
    
    cara5 = punMedioCara(3)
    c5 = text(text ="3",pos = vector(cara5[0],cara5[1],cara5[2]),color=color.red, height=0.2 , billboard=True)
    #mostramos por pantalla las caras
    '''
    #fin piramide
    
    #poliedro 14 vertices
    '''
    centroide = sphere(pos = vector(0,0,0), color = color.purple, radius = 0.1)
    
    posVert = np.array([[1,-1,1],           #0
                        [-1,-1,1],          #1
                        [-1,-1,-1],         #2
                        [1,-1,-1],          #3
                        [1.5,0,1.5],        #4
                        [-1.5,0,1.5],       #5
                        [-1.5,0,-1.5],      #6
                        [1.5,0,-1.5],       #7
                        [1,1,1],            #8
                        [-1,1,1],           #9
                        [-1,1,-1],          #10
                        [1,1,-1]])
    
    Va = np.array([[posA[0]+posVert[0][0],posA[1]+posVert[0][1],posA[2]+posVert[0][2]],     #0
                   [posA[0]+posVert[1][0],posA[1]+posVert[1][1],posA[2]+posVert[1][2]],     #1
                   [posA[0]+posVert[2][0],posA[1]+posVert[2][1],posA[2]+posVert[2][2]],     #2
                   [posA[0]+posVert[3][0],posA[1]+posVert[3][1],posA[2]+posVert[3][2]],     #3
                   [posA[0]+posVert[4][0],posA[1]+posVert[4][1],posA[2]+posVert[4][2]],     #4
                   [posA[0]+posVert[5][0],posA[1]+posVert[5][1],posA[2]+posVert[5][2]],     #5
                   [posA[0]+posVert[6][0],posA[1]+posVert[6][1],posA[2]+posVert[6][2]],     #6
                   [posA[0]+posVert[7][0],posA[1]+posVert[7][1],posA[2]+posVert[7][2]],     #7
                   [posA[0]+posVert[8][0],posA[1]+posVert[8][1],posA[2]+posVert[8][2]],     #8
                   [posA[0]+posVert[9][0],posA[1]+posVert[9][1],posA[2]+posVert[9][2]],     #9
                   [posA[0]+posVert[10][0],posA[1]+posVert[10][1],posA[2]+posVert[10][2]],  #10
                   [posA[0]+posVert[11][0],posA[1]+posVert[11][1],posA[2]+posVert[11][2]]])
    #Generamos los vetices en base a nuestro centroide de la prticula A
    
    aristas = np.array([[0,1],            #0
                        [1,2],            #1
                        [2,3],            #2
                        [3,0],            #3
                        [4,5],            #4
                        [5,6],            #5
                        [6,7],            #6
                        [7,4],            #7
                        [8,9],            #8
                        [9,10],           #9
                        [10,11],          #10
                        [11,8],          #11
                        [0,4],
                        [4,8],
                        [1,5],
                        [5,9],
                        [2,6],
                        [6,10],
                        [3,7],
                        [7,11]])
    #aristas particula B y A
    
    verticesA = [sphere(pos = vector(Va[0][0],Va[0][1],Va[0][2]), color = color.purple, radius = 0.1),
                 sphere(pos = vector(Va[1][0],Va[1][1],Va[1][2]), color = color.red, radius = 0.1),
                 sphere(pos = vector(Va[2][0],Va[2][1],Va[2][2]), color = color.blue, radius = 0.1),
                 sphere(pos = vector(Va[3][0],Va[3][1],Va[3][2]), color = color.yellow, radius = 0.1),
                 sphere(pos = vector(Va[4][0],Va[4][1],Va[4][2]), color = color.red, radius = 0.1),
                 sphere(pos = vector(Va[5][0],Va[5][1],Va[5][2]), color = color.blue, radius = 0.1),
                 sphere(pos = vector(Va[6][0],Va[6][1],Va[6][2]), color = color.yellow, radius = 0.1),
                 sphere(pos = vector(Va[7][0],Va[7][1],Va[7][2]), color = color.purple, radius = 0.1),
                 sphere(pos = vector(Va[8][0],Va[8][1],Va[8][2]), color = color.red, radius = 0.1),
                 sphere(pos = vector(Va[9][0],Va[9][1],Va[9][2]), color = color.blue, radius = 0.1),
                 sphere(pos = vector(Va[10][0],Va[10][1],Va[10][2]), color = color.yellow, radius = 0.1),
                 sphere(pos = vector(Va[11][0],Va[11][1],Va[11][2]), color = color.purple, radius = 0.1)]
    #vertices de la particula A mostrados por pantalla
    
    aristasA = [arrow(pos = vector(Va[aristas[0][0]][0],Va[aristas[0][0]][1],Va[aristas[0][0]][2]), axis = vector(Va[aristas[0][1]][0],Va[aristas[0][1]][1],Va[aristas[0][1]][2]) - vector(Va[aristas[0][0]][0],Va[aristas[0][0]][1],Va[aristas[0][0]][2]), color = color.magenta, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[1][0]][0],Va[aristas[1][0]][1],Va[aristas[1][0]][2]), axis = vector(Va[aristas[1][1]][0],Va[aristas[1][1]][1],Va[aristas[1][1]][2]) - vector(Va[aristas[1][0]][0],Va[aristas[1][0]][1],Va[aristas[1][0]][2]), color = color.purple, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[2][0]][0],Va[aristas[2][0]][1],Va[aristas[2][0]][2]), axis = vector(Va[aristas[2][1]][0],Va[aristas[2][1]][1],Va[aristas[2][1]][2]) - vector(Va[aristas[2][0]][0],Va[aristas[2][0]][1],Va[aristas[2][0]][2]), color = color.yellow, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[3][0]][0],Va[aristas[3][0]][1],Va[aristas[3][0]][2]), axis = vector(Va[aristas[3][1]][0],Va[aristas[3][1]][1],Va[aristas[3][1]][2]) - vector(Va[aristas[3][0]][0],Va[aristas[3][0]][1],Va[aristas[3][0]][2]), color = color.blue, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[4][0]][0],Va[aristas[4][0]][1],Va[aristas[4][0]][2]), axis = vector(Va[aristas[4][1]][0],Va[aristas[4][1]][1],Va[aristas[4][1]][2]) - vector(Va[aristas[4][0]][0],Va[aristas[4][0]][1],Va[aristas[4][0]][2]), color = color.green, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[5][0]][0],Va[aristas[5][0]][1],Va[aristas[5][0]][2]), axis = vector(Va[aristas[5][1]][0],Va[aristas[5][1]][1],Va[aristas[5][1]][2]) - vector(Va[aristas[5][0]][0],Va[aristas[5][0]][1],Va[aristas[5][0]][2]), color = color.orange, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[6][0]][0],Va[aristas[6][0]][1],Va[aristas[6][0]][2]), axis = vector(Va[aristas[6][1]][0],Va[aristas[6][1]][1],Va[aristas[6][1]][2]) - vector(Va[aristas[6][0]][0],Va[aristas[6][0]][1],Va[aristas[6][0]][2]), color = color.red, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[7][0]][0],Va[aristas[7][0]][1],Va[aristas[7][0]][2]), axis = vector(Va[aristas[7][1]][0],Va[aristas[7][1]][1],Va[aristas[7][1]][2]) - vector(Va[aristas[7][0]][0],Va[aristas[7][0]][1],Va[aristas[7][0]][2]), color = color.cyan, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[8][0]][0],Va[aristas[8][0]][1],Va[aristas[8][0]][2]), axis = vector(Va[aristas[8][1]][0],Va[aristas[8][1]][1],Va[aristas[8][1]][2]) - vector(Va[aristas[8][0]][0],Va[aristas[8][0]][1],Va[aristas[8][0]][2]), color = color.green, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[9][0]][0],Va[aristas[9][0]][1],Va[aristas[9][0]][2]), axis = vector(Va[aristas[9][1]][0],Va[aristas[9][1]][1],Va[aristas[9][1]][2]) - vector(Va[aristas[9][0]][0],Va[aristas[9][0]][1],Va[aristas[9][0]][2]), color = color.orange, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[10][0]][0],Va[aristas[10][0]][1],Va[aristas[10][0]][2]), axis = vector(Va[aristas[10][1]][0],Va[aristas[10][1]][1],Va[aristas[10][1]][2]) - vector(Va[aristas[10][0]][0],Va[aristas[10][0]][1],Va[aristas[10][0]][2]), color = color.red, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[11][0]][0],Va[aristas[11][0]][1],Va[aristas[11][0]][2]), axis = vector(Va[aristas[11][1]][0],Va[aristas[11][1]][1],Va[aristas[11][1]][2]) - vector(Va[aristas[11][0]][0],Va[aristas[11][0]][1],Va[aristas[11][0]][2]), color = color.cyan, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[12][0]][0],Va[aristas[12][0]][1],Va[aristas[12][0]][2]), axis = vector(Va[aristas[12][1]][0],Va[aristas[12][1]][1],Va[aristas[12][1]][2]) - vector(Va[aristas[12][0]][0],Va[aristas[12][0]][1],Va[aristas[12][0]][2]), color = color.red, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[13][0]][0],Va[aristas[13][0]][1],Va[aristas[13][0]][2]), axis = vector(Va[aristas[13][1]][0],Va[aristas[13][1]][1],Va[aristas[13][1]][2]) - vector(Va[aristas[13][0]][0],Va[aristas[13][0]][1],Va[aristas[13][0]][2]), color = color.cyan, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[14][0]][0],Va[aristas[14][0]][1],Va[aristas[14][0]][2]), axis = vector(Va[aristas[14][1]][0],Va[aristas[14][1]][1],Va[aristas[14][1]][2]) - vector(Va[aristas[14][0]][0],Va[aristas[14][0]][1],Va[aristas[14][0]][2]), color = color.red, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[15][0]][0],Va[aristas[15][0]][1],Va[aristas[15][0]][2]), axis = vector(Va[aristas[15][1]][0],Va[aristas[15][1]][1],Va[aristas[15][1]][2]) - vector(Va[aristas[15][0]][0],Va[aristas[15][0]][1],Va[aristas[15][0]][2]), color = color.cyan, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[16][0]][0],Va[aristas[16][0]][1],Va[aristas[16][0]][2]), axis = vector(Va[aristas[16][1]][0],Va[aristas[16][1]][1],Va[aristas[16][1]][2]) - vector(Va[aristas[16][0]][0],Va[aristas[16][0]][1],Va[aristas[16][0]][2]), color = color.red, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[17][0]][0],Va[aristas[17][0]][1],Va[aristas[17][0]][2]), axis = vector(Va[aristas[17][1]][0],Va[aristas[17][1]][1],Va[aristas[17][1]][2]) - vector(Va[aristas[17][0]][0],Va[aristas[17][0]][1],Va[aristas[17][0]][2]), color = color.cyan, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[18][0]][0],Va[aristas[18][0]][1],Va[aristas[18][0]][2]), axis = vector(Va[aristas[18][1]][0],Va[aristas[18][1]][1],Va[aristas[18][1]][2]) - vector(Va[aristas[18][0]][0],Va[aristas[18][0]][1],Va[aristas[18][0]][2]), color = color.red, shaftwidth = 0.05),
                arrow(pos = vector(Va[aristas[19][0]][0],Va[aristas[19][0]][1],Va[aristas[19][0]][2]), axis = vector(Va[aristas[19][1]][0],Va[aristas[19][1]][1],Va[aristas[19][1]][2]) - vector(Va[aristas[19][0]][0],Va[aristas[19][0]][1],Va[aristas[19][0]][2]), color = color.cyan, shaftwidth = 0.05)]
    
    #aristas de la particula A mostradas por pantalla
    '''
    
    
    
    '''
    #mostramos el vertices mas cercano al plano y su vector a la proyeccion de él
    prueba = sphere(pos = vector(PPA[0],PPA[1],PPA[2]), color = color.white, radius = 0.1)
    hola = arrow(pos = vector(P0[0],P0[1],P0[2]), axis = vector(PPA[0],PPA[1],PPA[2]) - vector(P0[0],P0[1],P0[2]), color = color.green, shaftwidth = 0.1, opacity = 0.1)
    prueba1 = sphere(pos = vector(PPB[0],PPB[1],PPB[2]), color = color.white, radius = 0.1)
    hola1 = arrow(pos = vector(Q0[0],Q0[1],Q0[2]), axis = vector(PPB[0],PPB[1],PPB[2]) - vector(Q0[0],Q0[1],Q0[2]), color = color.green, shaftwidth = 0.1, opacity = 0.1)
    '''
    '''
    hola = SL(posA,posB)
    print(hola)
    print(distancia(hola, posB))
    #print(distancia([0.9,1,0],posB))
    SLpunto = sphere(pos = vector(hola[0],hola[1],hola[2]), color = color.red, radius = 0.1)
    SLm = arrow(pos = SLpunto.pos, axis = cParB.pos - SLpunto.pos, color = color.white, shaftwidth = 0.05)
    '''
    '''
    ghost = punAleaAris([Va[3],Va[0]],0.96)
    print("\n")
    print(distancia(ghost,posB))
    print(distancia(Va[0],posB))
    print("\n")
    SLpunto = sphere(pos = vector(ghost[0],ghost[1],ghost[2]), color = color.red, radius = 0.1)
    '''

#a = button(text="Inicio", pos=scene.title_anchor, bind = inicio)

#triangulo equilatero
v1 = sphere(pos = vector(-1,1,-1), color = color.purple, radius = 0.1)
v2 = sphere(pos = vector(1,1,-1), color = color.blue, radius = 0.1)
v3 = sphere(pos = vector(0,1,0.73), color = color.red, radius = 0.1)

arrow(pos = v1.pos, axis = v2.pos - v1.pos, color = color.magenta, shaftwidth = 0.05)
arrow(pos = v2.pos, axis = v3.pos - v2.pos, color = color.magenta, shaftwidth = 0.05)
arrow(pos = v3.pos, axis = v1.pos - v3.pos, color = color.magenta, shaftwidth = 0.05)

arrow(pos = v1.pos, axis = vector(-2.23205081,1,-0.1339746) - v1.pos, color = color.green, shaftwidth = 0.05)
arrow(pos = v1.pos, axis = vector(-1,2,-1) - v1.pos, color = color.green, shaftwidth = 0.05)
arrow(pos = v1.pos, axis = vector(-0.73039247,1,-2.11341592) - v1.pos, color = color.green, shaftwidth = 0.05)

#arrow(pos = v3.pos, axis = vector(2.23205081,1,-0.1339746) - v1.pos, color = color.green, shaftwidth = 0.05)
#arrow(pos = v3.pos, axis = vector(1,2,-1) - v1.pos, color = color.green, shaftwidth = 0.05)
arrow(pos = v3.pos, axis = vector(0.73039247, 1, 2.11341592) - v3.pos, color = color.green, shaftwidth = 0.05)