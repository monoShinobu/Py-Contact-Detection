import numpy as np
from vpython import *
import figuras as fig
import math as ma
import time

def planoCartesiano():
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


def rotacion(angu, eje, rotacionX, rotacionY, rotacionZ):#generamos el punto rotado
    if(eje == "x"):
        rotacionX[1][1] = np.cos(angu)
        rotacionX[1][2] = np.sin(angu) * -1
        rotacionX[2][1] = np.sin(angu)
        rotacionX[2][2] = np.cos(angu)
    elif(eje == "y"):
        rotacionY[0][0] = np.cos(angu)
        rotacionY[0][2] = np.sin(angu) * -1
        rotacionY[2][0] = np.sin(angu)
        rotacionY[2][2] = np.cos(angu)
    elif(eje == "z"):
        rotacionZ[0][0] = np.cos(angu)
        rotacionZ[0][1] = np.sin(angu) * -1
        rotacionZ[1][0] = np.sin(angu)
        rotacionZ[1][1] = np.cos(angu)
    matRota = np.dot(rotacionZ, np.dot(rotacionY, rotacionX))
    return matRota, rotacionX, rotacionY, rotacionZ

def creaPlano(puntoPlano, puntoRef):
    dis = [puntoRef[0] - puntoPlano[0], puntoRef[1] - puntoPlano[1], puntoRef[2] - puntoPlano[2]]
    #es el vector distancia entre el plano y el centroide B
    
    moPlano = np.sqrt(np.power(dis[0],2) + np.power(dis[1],2) + np.power(dis[2],2))
    #calculamos el modulo de un vector del plano
    
    dNormal = [dis[0]/moPlano, dis[1]/moPlano, dis[2]/moPlano]
    #vector normal del plano al centroide B
    
    d = (dNormal[0]*puntoPlano[0] + dNormal[1]*puntoPlano[1] + dNormal[2]*puntoPlano[2]) * -1
    #calculamos d en base a la ecuacion del plano
    
    return dNormal, d

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

#se crea una proyeccion de un punto P en una arista AB
def proyecArista(A, B, P):
    AP = P - A
    AB = B - A
    
    dotAPAB = np.dot(AP, AB)
    dotABAB = np.dot(AB, AB)
    
    p = A + ( ( dotAPAB / (dotABAB) ) * AB )
    
    return p

def punMedioCaraParticula(cara, Va, carasVertices, vertCaras):#buscamos el punto medio de un cara

    suma = Va[carasVertices[cara][0]]
    
    for i in range(1, vertCaras):
        suma = suma + Va[carasVertices[cara][i]]
    
    PaFi = suma / len(carasVertices[cara])
    
    return PaFi

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

def dentro(P,car, otro):#entra un punto y una cara para ver si el punto esta dentro de ella
    
    suma = 0
    
    
    for i in range(len(carasVertices[car])):
        #time.sleep(1)
        
        if i == len(carasVertices[car]) - 1:
            ve1 =Va[carasVertices[car][i]]
            ve2 = Va[carasVertices[car][0]]
        else:
            ve1 = Va[carasVertices[car][i]]
            ve2 = Va[carasVertices[car][i+1]]
        
        vector1 = ve1 - P
        vector2 = ve2 - P
        #vector1 = np.array([ve1[0]-P[0],ve1[1]-P[1],ve1[2]-P[2]])
        #vector2 = np.array([ve2[0]-P[0],ve2[1]-P[1],ve2[2]-P[2]])
        
        top = np.dot(vector1, vector2)
        bot1 = np.sqrt((vector1[0]**2) + (vector1[1]**2) + (vector1[2]**2))
        bot2 = np.sqrt((vector2[0]**2) + (vector2[1]**2) + (vector2[2]**2))
        
        if bot1 == 0 or bot2 == 0:
            suma = 360
            break
        else:
            angu = ma.degrees(np.arccos(top/(bot1*bot2)))
            suma = angu + suma
        
    
    if suma > 359 and suma < 361:
        estaDentro = 1
    else:
        estaDentro = 0
    
    '''
    estaDentro = 1
    
    if otro == 314:
        a1 = arrow(pos = vector(1,1,1), axis = vector(1,1,1) - vector(1,1,1), shaftwidth = 0.2)
        a2 = arrow(pos = vector(1,1,1), axis = vector(1,1,1) - vector(1,1,1), shaftwidth = 0.2)
        a3 = arrow(pos = vector(1,1,1), axis = vector(1,1,1) - vector(1,1,1), shaftwidth = 0.2)
        print("/////////////////////////////\n")
    
    for i in range(len(caras[car])):
        aris = np.array([Va[aristas[caras[car][i]][0]], Va[aristas[caras[car][i]][1]]])
        proye = proyecArista(aris[0], aris[1], P)
        t = calculoT(proye, aris)
        
        if otro == 314:
            print(aris)
            if i == 0:
                a1.pos = vector(aris[0][0], aris[0][1], aris[0][2])
                a1.axis = vector(aris[1][0], aris[1][1], aris[1][2]) - vector(aris[0][0], aris[0][1], aris[0][2])
            if i == 1:
                a2.pos = vector(aris[0][0], aris[0][1], aris[0][2])
                a2.axis = vector(aris[1][0], aris[1][1], aris[1][2]) - vector(aris[0][0], aris[0][1], aris[0][2])
            if i == 2:
                a3.pos = vector(aris[0][0], aris[0][1], aris[0][2])
                a3.axis = vector(aris[1][0], aris[1][1], aris[1][2]) - vector(aris[0][0], aris[0][1], aris[0][2])
        
        if t > 1 or t < 0:
            print("Hola")
            estaDentro = 0
            break
    if otro == 314:
        print("/////////////////////////////\n")
    '''
    return estaDentro

def zonaCritica(ari1, ari2, punto): #entran las 2 aristas y un punto en el espacio
    
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
    '''
    print("vertMenor: ", vertMenor)
    print("disMenor: ", disMenor)
    print("\n")
    '''
    for i in range(len(Va)-2):
        vertAux = Va[i]
        disAux = distancia(vertAux, punto)
        #print(vertAux)
        #print(disAux,"\n")
        if disAux < disMenor[0] and disMenor[0] >= disMenor[1]:
            disMenor[0] = disAux
            vertMenor[0] = vertAux
        elif disAux < disMenor[1] and disMenor[1] >= disMenor[0]:
            disMenor[1] = disAux
            vertMenor[1] = vertAux
    return vertMenor

def SL(centroide, punto, parti, otro):
    global Va, caras, carasVertices, caras, aristas
    Va = parti.vertices
    caras = parti.caras
    carasVertices = parti.carasVertices
    aristas = parti.aristas
    
    caraDistanciaMenor = 0#elegimos la primera cara por defecto
    distanciaCara = distancia(punMedioCara(0), punto)
    #print("\nprimera dist = ",distanciaCara)
    '''
    p1 = sphere(pos = vector(punMedioCara(0)[0],punMedioCara(0)[1],punMedioCara(0)[2]), color = color.cyan, radius = 0.15)
    a1 = arrow(pos = vector(punMedioCara(0)[0],punMedioCara(0)[1],punMedioCara(0)[2]), axis = vector(punto[0],punto[1],punto[2]) - vector(punMedioCara(0)[0],punMedioCara(0)[1],punMedioCara(0)[2]),shaftwidth = 0.1)
    p2 = sphere(pos = vector(1,1,1), color = color.cyan, radius = 0.15)
    a2 = arrow(pos = vector(1,1,1), axis = vector(1,1,1) - vector(1,1,1),shaftwidth = 0.1)
    '''
    for i in range(1, len(caras)):#el ciclo va desde la segunda cara a la ultima
        disAux = distancia(punMedioCara(i), punto)
        #print("Dist = ", disAux)
        if disAux < distanciaCara:
            '''
            p2.pos = vector(punMedioCara(i)[0],punMedioCara(i)[1],punMedioCara(i)[2])
            a2.pos = vector(punMedioCara(i)[0],punMedioCara(i)[1],punMedioCara(i)[2])
            a2.axis = vector(punto[0],punto[1],punto[2]) - vector(punMedioCara(i)[0],punMedioCara(i)[1],punMedioCara(i)[2])
            '''
            distanciaCara = disAux
            caraDistanciaMenor = i
            #print("\n Cara = ",i)
    '''
    if otro != 314:
        p1.visible = False
        a1.visible = False
        p2.visible = False
        a2.visible = False
    
    print("\n\n\n\n\n","caraDistanciaMenor",caraDistanciaMenor)
    print("distanciaCara",distanciaCara,"\n\n\n\n\n")
    '''
    print("///////////////////////\n","caraDistanciaMenor = ",caraDistanciaMenor,"\n///////////////////////")
    #punMedio = punMedioCara(caraDistanciaMenor)#punto medio de la cara
    caraPlano = parti.posCaraPlano[caraDistanciaMenor]
    
    puntoProyectado = proyecRPlano(caraPlano, centroide, punto)
    
    #SLpunto = sphere(pos = vector(puntoProyectado[0],puntoProyectado[1],puntoProyectado[2]), color = color.green, radius = 0.1)
    estaDentro = dentro(puntoProyectado, caraDistanciaMenor, otro)
    '''
    print("\n\n------------")
    print("caraDistanciaMenor: ",caraDistanciaMenor)
    print("------------\n\n")
    '''
    ##print("\n-------------------------------------------\nCasos\n")
    if estaDentro == 1:
        Pn = puntoProyectado
        print("Caso 1 ", otro)
    else:
        vertMenor = menorVertice(punto)
        '''
        print("\n\n------------")
        print("vertMenor: ",vertMenor)
        print("------------\n\n")
        '''
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
            print("Caso 3", otro)
        else:
            #vectorAB = np.array([vertMenor[1][0]-vertMenor[0][0],vertMenor[1][1]-vertMenor[0][1],vertMenor[1][2]-vertMenor[0][2]])
            ##vectorAB = vertMenor[1] - vertMenor[0]
            #vectorAP = np.array([punto[0] - vertMenor[0][0],punto[1] - vertMenor[0][1],punto[2] - vertMenor[0][2]])
            ##vectorAP = punto - vertMenor[0]
            #Pn = vertMenor[0] + (np.dot(vectorAP,vectorAB) / np.dot(vectorAB,vectorAB)) * vectorAB
            Pn = proyecArista(vertMenor[0], vertMenor[1], punto)
            print("Caso 2", otro)
            '''
            punMedio = punMedioCara(caraDistanciaMenor2)#punto medio de la cara
            puntoProyectado = proyecRPlano(punMedio, centroide, puntoProyectado)
            Pn = puntoProyectado
            '''
    ##print("---------------------\n\n")
    return Pn, caraDistanciaMenor

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
        p0 = (100,100,-100)
    
    if u < 1 and u > 0:
        p1 = c + u * s
    else:
        p1 = (100,100,100)
    
    return p0, p1
'''
def aristaMenor(numVertA, numVertB, parti1, parti2, punMedio, posA, posB):
    
    distAux = 1000
    print("**************************************************")
    #p1 = sphere(pos = vector(1,1,1), color = color.cyan, radius = 0.15)
    #p2 = sphere(pos = vector(1,1,1), color = color.red, radius = 0.15)
    
    for i in range(len(parti1.verticesArista[numVertA])):
        ariMid = parti1.posAriMed[parti1.verticesArista[numVertA][i]]
        
        proye = proyecRPlano(posB, posA, ariMid)
        
        dist = distancia(ariMid, proye)
        #dist = distancia(ariMid, parti2.vertices[numVertB])
        
        if dist < distAux:
            ariCerA = np.array([parti1.vertices[parti1.aristas[parti1.verticesArista[numVertA][i]][0]], parti1.vertices[parti1.aristas[parti1.verticesArista[numVertA][i]][1]]])
            i2 = i
            #p1.pos = vector(ariMid[0], ariMid[1], ariMid[2])
        distAux = dist
        
    print("Ari 1 = ", parti1.verticesArista[numVertA][i2])
    distAux = 1000
    
    for i in range(len(parti2.verticesArista[numVertB])):
        ariMid = parti2.posAriMed[parti2.verticesArista[numVertB][i]]
        
        proye = proyecRPlano(posA, posB, ariMid)
        
        dist = distancia(ariMid, proye)
        
        if dist < distAux:
            ariCerB = np.array([parti2.vertices[parti2.aristas[parti2.verticesArista[numVertB][i]][0]], parti2.vertices[parti2.aristas[parti2.verticesArista[numVertB][i]][1]]])
            i3 = i
            #p2.pos = vector(ariMid[0], ariMid[1], ariMid[2])
        distAux = dist
        
    print("Ari 2 = ", parti2.verticesArista[numVertB][i3])
        
    print("**************************************************")
    return ariCerA, ariCerB
'''

'''
def aristaMenor(parti1, parti2, dNormal, d):
    
    disMenorA = 1000
    disMenorB = 1000
    
    for i in range(0, len(parti1.aristas)):
        
        vertA1 = parti1.vertices[parti1.aristas[i][0]]
        vertA2 = parti1.vertices[parti1.aristas[i][1]]
        
        proVertA1 = proyeccion(vertA1, dNormal, d)
        proVertA2 = proyeccion(vertA2, dNormal, d)
        
        distA1 = distancia(vertA1, proVertA1)
        distA2 = distancia(vertA2, proVertA2)
        
        distA = distA1 + distA2
        
        if distA < disMenorA:
            ariCerA = np.array([vertA1, vertA2]) #arista de A mas cercana al plano
            hola = i
            disMenorA = distA
    
    for i in range(0, len(parti2.aristas)):
        
        vertB1 = parti2.vertices[parti2.aristas[i][0]]
        vertB2 = parti2.vertices[parti2.aristas[i][1]]
        
        proVertB1 = proyeccion(vertB1, dNormal, d)
        proVertB2 = proyeccion(vertB2, dNormal, d)
        
        distB1 = distancia(vertB1, proVertB1)
        distB2 = distancia(vertB2, proVertB2)
        
        distB = distB1 + distB2
        
        if distB < disMenorB:
            ariCerB = np.array([vertB1, vertB2]) #arista de A mas cercana al plano
            disMenorB = distB
            hola2 = i
            
        #print("\nArista1 = ", hola, "\nArista2 = ", hola2)
    return ariCerA, ariCerB
'''
def aristaMenor(numVertA, numVertB, parti1, parti2):
    distAux = 1000
    i2 = 0
    j2 = 0
    Pi0 = np.array([0.0,0.0,0.0])
    Qi0 = np.array([0.0,0.0,0.0])
    for i in range(len(parti1.verticesArista[numVertA])):
        ari1 = np.array([parti1.vertices[parti1.aristas[parti1.verticesArista[numVertA][i]][0]], 
                         parti1.vertices[parti1.aristas[parti1.verticesArista[numVertA][i]][1]]])
        
        for j in range(len(parti2.verticesArista[numVertB])):
            ari2 = np.array([parti2.vertices[parti2.aristas[parti2.verticesArista[numVertB][j]][0]], 
                             parti2.vertices[parti2.aristas[parti2.verticesArista[numVertB][j]][1]]])
            P0, P1 = contactoAristas(ari1 , ari2)
            dist = distancia(P0, P1)
            if dist < distAux:
                    if P0[0] == 100 or P1[0] == 100:
                        print("Hola")
                    else:
                        Pi0 = P0
                        Qi0 = P1
                        i2 = i
                        j2 = j
                        distAux = dist
                    

    print("Ari 1 = ", parti1.verticesArista[numVertA][i2])
    print("Ari 2 = ", parti2.verticesArista[numVertB][j2])
    return distAux, Pi0, Qi0

















