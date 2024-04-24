import vpython as v
import random as ran
import numpy as np
import math as ma
import funcionesSLM as f
import figuras as fig
import time

v.scene.title = "SLM, por Jaime Velásquez\n"

'''
parti = box(opacity = 0.5, pos = vector(2.5,2.5,2.5), size = vector(5,5,5))
punto = sphere(pos = vector(7,0,0), color = color.green, radius = 0.6)
pO = sphere(pos = vector(0.5,5,5), radius = 0.6)
PQ = arrow(pos = pO.pos, axis = punto.pos - pO.pos)
'''

#f.planoCartesiano()

#generamos los elmentos de SLM que se mostraran por pantalla, pero ocultos
qi = np.array([0.0,0.0,0.0])
pi = np.array([0.0,0.0,0.0])
graSL = fig.grapSLM.grapSLM(qi, pi)



def calculoT(pun, ari):
    t = (((pun[0]-ari[0][0])+(pun[1]-ari[0][1])+(pun[2]-ari[0][2]))/((ari[1][0]-ari[0][0])+(ari[1][1]-ari[0][1])+(ari[1][2]-ari[0][2])+0.0001))
    return t


def selectFigura(m):
    global parti1, parti2
    val = m.selected
    if m.p == 1:
        parti1.delete()
        if val == "Cubo":
            parti1 = fig.cubo.cubo(posA)
        elif val == "Tetraedro":
            parti1 = fig.tetraedro.tetraedro(posA)
        elif val == "Piramide":
            parti1 = fig.piramide.piramide(posA)
    else:
        parti2.delete()
        if val == "Cubo":
            parti2 = fig.cubo.cubo(posB)
        elif val == "Tetraedro":
            parti2 = fig.tetraedro.tetraedro(posB)
        elif val == "Piramide":
            parti2 = fig.piramide.piramide(posB)

v.scene.caption = "Particula A                                                                                     Particula B\n"
v.scene.append_to_caption('\n')
#pedimos que el usuario defina la forma que van a tener las particulas
p = 0
menuFig1 = v.menu(choices=["Cubo", "Tetraedro", "Piramide"], index=0, bind=selectFigura, p = 1)
v.scene.append_to_caption('                                                                                  ')
menuFig2 = v.menu(choices=["Cubo", "Tetraedro", "Piramide"], index=0, bind=selectFigura, p = 2)
v.scene.append_to_caption('\n\n')




#definimos la rotacion que van a tener las particulas
v.scene.append_to_caption('Rotaciones\n\n')
def setRotaPar1(s):
    wt1.text = '{:1d}'.format(s.value)

def setRotaPar2(s):
    wt2.text = '{:1d}'.format(s.value)

sliRotaAX = v.slider(min = 0, max = 359, step = 1, value = 0, lenght = 150, bind = setRotaPar1)
wt1 = v.wtext(text='{:1d}'.format(sliRotaAX.value))
v.scene.append_to_caption('° en X')

v.scene.append_to_caption('               ')

sliRotaBX = v.slider(min = 0, max = 359, step = 1, value = 0, lenght = 150, bind = setRotaPar2)
wt2 = v.wtext(text='{:1d}'.format(sliRotaBX.value))
v.scene.append_to_caption('° en X\n\n')


def setRotaPar3(s):
    wt3.text = '{:1d}'.format(s.value)

def setRotaPar4(s):
    wt4.text = '{:1d}'.format(s.value)

sliRotaAY = v.slider(min = 0, max = 359, step = 1, value = 0, lenght = 150, bind = setRotaPar3)
wt3 = v.wtext(text='{:1d}'.format(sliRotaAY.value))
v.scene.append_to_caption('° en Y')

v.scene.append_to_caption('               ')

sliRotaBY = v.slider(min = 0, max = 359, step = 1, value = 0, lenght = 150, bind = setRotaPar4)
wt4 = v.wtext(text='{:1d}'.format(sliRotaBY.value))
v.scene.append_to_caption('° en Y\n\n')


def setRotaPar5(s):
    wt5.text = '{:1d}'.format(s.value)

def setRotaPar6(s):
    wt6.text = '{:1d}'.format(s.value)

sliRotaAZ = v.slider(min = 0, max = 359, step = 1, value = 0, lenght = 150, bind = setRotaPar5)
wt5 = v.wtext(text='{:1d}'.format(sliRotaAZ.value))
v.scene.append_to_caption('° en Z')

v.scene.append_to_caption('               ')

sliRotaBZ = v.slider(min = 0, max = 359, step = 1, value = 0, lenght = 150, bind = setRotaPar6)
wt6 = v.wtext(text='{:1d}'.format(sliRotaBZ.value))
v.scene.append_to_caption('° en Z\n\n')



#deginimos la posicion de los centroides
posA = np.array([-3.0,0.0,0.0])
posB = np.array([3.0,0.0,0.0])
posBOriginal = posB

'''
#generamos aleatoriamente la posicion de los centroides
posA = np.array([ran.uniform(-5, 5),ran.uniform(-5, 5),ran.uniform(-5, 5)])
#posicion del centroide A
Vcc = 0
#Vcc corresponde a la distancia entre ambos centroides

while Vcc < 5:#ciclo se ejecuta hasta que la distancia entre el
                #centroide A y B sea mayor a 2,5
    posB = np.array([ran.uniform(-5, 5),ran.uniform(-5, 5),ran.uniform(-5, 5)])
    #generamos un punto aleatorio B
    Vcc = f.distancia(posA,posB)
'''

#slide para regular la distancia entre particulas
def dist(s):
    dt.text = '{:0.1f}'.format(s.value)

sliDistancia = v.slider(min = 0, max = f.distancia(posA, posB) * 2, value = f.distancia(posA, posB), lenght = 150, bind = dist)
dt = v.wtext(text='{:0.1f}'.format(sliDistancia.value))
v.scene.append_to_caption(' de distancia entre particulas')

def distSL(d):
    dSL.text = '{:0.2f}'.format(d)

v.scene.append_to_caption('                      ')
dSL = v.wtext(text='{:0.2f}'.format(0))
v.scene.append_to_caption(' de distancia para el SL')

#corresponde a un arreglo que contiene todos los valores que afectan al movimiento de la particula
valMovi = np.array([sliRotaAX.value, sliRotaBX.value, sliRotaAY.value, sliRotaBY.value, sliRotaAZ.value, sliRotaBZ.value, sliDistancia.value])

#arreglo que contendra los valores antiguos
valMovi0 = np.array([361, 361, 361, 361, 361 ,361, 100])


part = np.array([v.sphere(pos = v.vector(posA[0],posA[1],posA[2]), color = v.color.green, radius = 0.1),
                 v.sphere(pos = v.vector(posB[0],posB[1],posB[2]), color = v.color.red, radius = 0.1)])
#mostramos por pantalla el centroide de la particula

VCC = v.arrow(pos = part[0].pos, axis = part[1].pos - part[0].pos, color = v.color.magenta, shaftwidth = 0.05)
#VCC corresponde al vector de centroide a centroide

nompart = np.array([v.text(text = "A", pos = v.vector(posA[0] + 0.1, posA[1] + 0.1, posA[2] + 0.1), color = v.color.white, height = 0.5 , billboard = True),
                    v.text(text = "B", pos = v.vector(posB[0] + 0.1, posB[1] + 0.1, posB[2] + 0.1), color = v.color.white, height = 0.5 , billboard = True)])
#mostramos por pantalla el nombre de la particula

parti1 = fig.cubo.cubo(posA)
parti2 = fig.cubo.cubo(posB)


puMedio = f.punAleaAris(np.array([posB, posA]), 0.5)

#pbp = v.box(pos = v.vector(puMedio[0], puMedio[1], puMedio[2]),axis = v.vector(posB[0],posB[1],posB[2]) - v.vector(posA[0],posA[1],posA[2]), length = 0.01, height= 5, width=5, opacity = 0.5)





'''
algo = v.sphere(pos = v.vector(1,2,3), color = v.color.purple, radius = 0.1)
algo3 = v.sphere(pos = v.vector(1,2,3), color = v.color.yellow, radius = 0.1)
algo2 = v.arrow(pos = v.vector(1,2,3), axis = v.vector(1,2,3) - v.vector(1,2,3), color = v.color.blue, shaftwidth = 0.05)
'''
pe0 = v.sphere(pos = v.vector(1,2,3), color = v.color.cyan, radius = 0.15)
qu0 = v.sphere(pos = v.vector(1,2,3), color = v.color.red, radius = 0.15)


#creamos el primer pbp en base al punto medio del vector centroide centroide
punMedio = [(posA[0]+posB[0])/2,(posA[1]+posB[1])/2,(posA[2]+posB[2])/2]

dNormal, d = f.creaPlano(punMedio, posB)

#creamos los valores del plano que va a estar siempre entre centroide centroide
dNormal2 = dNormal
d2 = d

while True:
    time.sleep(0.02)
    
    #aplicamos rotacion a las particulas
    rotacionAX = np.identity(3)
    rotacionAY = np.identity(3)
    rotacionAZ = np.identity(3)
    matRotaA = np.identity(3)

    matRotaA, rotacionAX, rotacionAY, rotacionAZ = f.rotacion(ma.radians(sliRotaAX.value), "x", rotacionAX, rotacionAY, rotacionAZ)
    matRotaA, rotacionAX, rotacionAY, rotacionAZ = f.rotacion(ma.radians(sliRotaAY.value), "y", rotacionAX, rotacionAY, rotacionAZ)
    matRotaA, rotacionAX, rotacionAY, rotacionAZ = f.rotacion(ma.radians(sliRotaAZ.value), "z", rotacionAX, rotacionAY, rotacionAZ)
    
    for i in range(len(parti1.vertices)):#actualizamos los valores de los vertices con la rotacion
        #print(posA, parti1.posVert[i], matRotaA)
        parti1.vertices[i] = posA + np.dot(matRotaA, parti1.posVert[i])
        parti1.vertices3D[i].pos = v.vector(parti1.vertices[i][0],parti1.vertices[i][1],parti1.vertices[i][2])
        parti1.numVertices[i].pos = v.vector(parti1.vertices[i][0],parti1.vertices[i][1] + 0.1,parti1.vertices[i][2])
        
    for i in range(len(parti1.aristas)):#actualizamos los valores de las aristas con la rotacion
        parti1.aristas3D[i].pos = v.vector(parti1.vertices[parti1.aristas[i][0]][0], parti1.vertices[parti1.aristas[i][0]][1], parti1.vertices[parti1.aristas[i][0]][2])
        parti1.aristas3D[i].axis = v.vector(parti1.vertices[parti1.aristas[i][1]][0], parti1.vertices[parti1.aristas[i][1]][1], parti1.vertices[parti1.aristas[i][1]][2]) - parti1.aristas3D[i].pos
        parti1.posAriMed[i] = f.punAleaAris(np.array([parti1.vertices[parti1.aristas[i][0]], parti1.vertices[parti1.aristas[i][1]]]),0.5)
        parti1.numAristas[i].pos = v.vector(parti1.posAriMed[i][0], parti1.posAriMed[i][1], parti1.posAriMed[i][2])
        
    for i in range(len(parti1.posCaraMed)):
        parti1.posCaraMed[i] = f.punMedioCaraParticula(i, parti1.vertices, parti1.carasVertices, len(parti1.caras[i]))
        parti1.numCaras[i].pos = v.vector(parti1.posCaraMed[i][0], parti1.posCaraMed[i][1] + 0.1, parti1.posCaraMed[i][2])
    
    
    
    
    rotacionBX = np.identity(3)
    rotacionBY = np.identity(3)
    rotacionBZ = np.identity(3)
    matRotaB = np.identity(3)
    
    matRotaB, rotacionBX, rotacionBY, rotacionBZ = f.rotacion(ma.radians(sliRotaBX.value), "x", rotacionBX, rotacionBY, rotacionBZ)
    matRotaB, rotacionBX, rotacionBY, rotacionBZ = f.rotacion(ma.radians(sliRotaBY.value), "y", rotacionBX, rotacionBY, rotacionBZ)
    matRotaB, rotacionBX, rotacionBY, rotacionBZ = f.rotacion(ma.radians(sliRotaBZ.value), "z", rotacionBX, rotacionBY, rotacionBZ)
    
    for i in range(len(parti2.vertices)):#actualizamos los valores de los vertices con la rotacion
        parti2.vertices[i] = posB + np.dot(matRotaB, parti2.posVert[i])
        parti2.vertices3D[i].pos = v.vector(parti2.vertices[i][0],parti2.vertices[i][1],parti2.vertices[i][2])
        parti2.numVertices[i].pos = v.vector(parti2.vertices[i][0],parti2.vertices[i][1] + 0.1,parti2.vertices[i][2])
        
    for i in range(len(parti2.aristas)):#actualizamos los valores de las aristas con la rotacion
        parti2.aristas3D[i].pos = v.vector(parti2.vertices[parti2.aristas[i][0]][0], parti2.vertices[parti2.aristas[i][0]][1], parti2.vertices[parti2.aristas[i][0]][2])
        parti2.aristas3D[i].axis = v.vector(parti2.vertices[parti2.aristas[i][1]][0], parti2.vertices[parti2.aristas[i][1]][1], parti2.vertices[parti2.aristas[i][1]][2]) - parti2.aristas3D[i].pos
        parti2.posAriMed[i] = f.punAleaAris(np.array([parti2.vertices[parti2.aristas[i][0]], parti2.vertices[parti2.aristas[i][1]]]),0.5)
        parti2.numAristas[i].pos = v.vector(parti2.posAriMed[i][0], parti2.posAriMed[i][1], parti2.posAriMed[i][2])
        
    for i in range(len(parti2.posCaraMed)):
        parti2.posCaraMed[i] = f.punMedioCaraParticula(i, parti2.vertices, parti2.carasVertices, len(parti2.caras[i]))
        parti2.numCaras[i].pos = v.vector(parti2.posCaraMed[i][0], parti2.posCaraMed[i][1] + 0.1, parti2.posCaraMed[i][2])
    parti1.actua()
    parti2.actua()
    
    
    
    
    
    disMenorA = 1000#distancia menor entre un vertice de A y su proyeccion en el plano
    disMenorB = 1000#distancia menor entre un vertice de B y su proyeccion en el plano
    
    #buscamos el vertice mas cercano al plano
    for i in range(0, len(parti1.vertices)):#buscamos el vertice mas cercano al plano
        proA = f.proyeccion(parti1.vertices[i], dNormal2, d2)
        vDistA = f.distancia(proA, parti1.vertices[i])
        
        if vDistA < disMenorA:
            P0 = parti1.vertices[i] #vertice de A mas cercano al plano
            PPA = proA #punto en el plano que es proyeccion del vertice A
            numVertA = i
            disMenorA = vDistA
    
    
    for i in range(0, len(parti2.vertices)):
        #buscamos el vertice mas cercano ahora tambien para B
        proB = f.proyeccion(parti2.vertices[i], dNormal2, d2)
        vDistB = f.distancia(proB, parti2.vertices[i])
        
        if vDistB < disMenorB:
            Q0 = parti2.vertices[i] #vertice de A mas cercano al plano
            PPB = proB #punto en el plano que es proyeccion del vertice A
            numVertB = i
            disMenorB = vDistB
    '''
    for i in range(0, len(parti2.aristas)):
        #buscamos el vertice mas cercano ahora tambien para B
        medAri = f.punAleaAris(np.array([parti2.vertices[parti2.aristas[i][0]], parti2.vertices[parti2.aristas[i][1]]]) , 0.5)
        proB = f.proyeccion(medAri, dNormal, d)
        vDistB = f.distancia(proB, medAri)
        
        if vDistB < disMenorB:
            Q0 = medAri #vertice de A mas cercano al plano
            PPB = proB #punto en el plano que es proyeccion del vertice A
            disMenorB = vDistB
    '''
    
    disMenorA = 1000#distancia menor entre un vertice de A y su proyeccion en el plano
    disMenorB = 1000#distancia menor entre un vertice de B y su proyeccion en el plano
    
    '''
    for i in range(0, len(parti1.aristas)):
        #buscamos el vertice mas cercano ahora tambien para B
        medAriA = f.punAleaAris(np.array([parti1.vertices[parti1.aristas[i][0]], parti1.vertices[parti1.aristas[i][1]]]) , 0.5)
        proA = f.proyeccion(medAriA, dNormal2, d2)
        vDistA = f.distancia(proA, medAriA)
        
        if vDistA < disMenorA:
            ariCerA = parti1.vertices[parti1.aristas[i][0]], parti1.vertices[parti1.aristas[i][1]] #arista de A mas cercana al plano
            hola = i
            disMenorA = vDistA
    
    for i in range(0, len(parti2.aristas)):
        #buscamos el vertice mas cercano ahora tambien para B
        medAriB = f.punAleaAris(np.array([parti2.vertices[parti2.aristas[i][0]], parti2.vertices[parti2.aristas[i][1]]]) , 0.5)
        proB = f.proyeccion(medAriB, dNormal2, d2)
        vDistB = f.distancia(proB, medAriB)
        
        if vDistB < disMenorB:
            ariCerB = parti2.vertices[parti2.aristas[i][0]], parti2.vertices[parti2.aristas[i][1]] #vertice de b mas cercano al plano
            hola2 = i
            disMenorB = vDistB
    '''
    
    
    #actualizamos la posicion del centroide B
    posB = f.punAleaAris(np.array([posA, posBOriginal]), sliDistancia.value / 6)
    distPartActual = sliDistancia.value
    
    if np.array_equal(valMovi, valMovi0) != True:
        
        #ariCerA, ariCerB = f.aristaMenor(parti1, parti2, dNormal2, d2)
        #ariCerA2, ariCerB2 = f.aristaMenor(parti1, parti2, dNormal, d)
        
        ariDis, Pi0, Qi0 = f.aristaMenor(numVertA, numVertB, parti1, parti2)
        

        #ariAri = f.contactoAristas(ariCerA, ariCerB)
        #ariAri2 = f.contactoAristas(ariCerA2, ariCerB2)
        
        pi1, caraA = f.SL(posA, Q0, parti1, "A")
        qi1, caraB = f.SL(posB, P0, parti2, "B")
        '''
        print("\n------------------\nCaraA = ",caraA)
        print("CaraB = ",caraB,"\n")
        '''
        
        distanciasFinales = np.array([f.distancia(pi1,Q0), f.distancia(qi1,P0), f.distancia(P0, Q0), 
                                      f.distancia(pi1, qi1), ariDis, 
                                      f.distancia(parti1.posCaraMed[caraA],parti2.posCaraMed[caraB])])
        
        
        #print("\n----------------------\nDistancias para comparacion")
        '''
        if (ariAri[0][0] != 100 and ariAri[1][0] != 100):
            ariDis = f.distancia(ariAri[0], ariAri[1])
        else:
            ariDis = 100
        '''
        '''
        if (ariAri2[0][0] != 100 and ariAri2[1][0] != 100):
            ariDis2 = f.distancia(ariAri2[0], ariAri2[1])
        else:
            ariDis2 = 100
        
            
            
            
        if ariDis != 100 and ariDis2 != 100:
            if ariDis < ariDis2:
                distanciasFinales[4] = ariDis
            else:
                distanciasFinales[4] = ariDis2
                ariAri = ariAri2
        elif ariDis != 100:
            distanciasFinales[4] = ariDis
        elif ariDis2 != 100:
            distanciasFinales[4] = ariDis2
            ariAri = ariAri2
        '''
        '''
        if ariDis != 100:
            distanciasFinales[4] = ariDis
        '''
        
        
        #print("dist = ", distanciasFinales,"\n")
        
        resul = np.where(distanciasFinales == np.amin(distanciasFinales))
        
        if resul[0][0] == 0:
            pi = pi1
            qi = Q0
            print("Part 1")
        elif resul[0][0] == 1:
            pi = P0
            qi = qi1
            print("Part 2")
        elif resul[0][0] == 2:
            pi = P0
            qi = Q0
            print("Part 3")
        elif resul[0][0] == 3:
            pi = pi1
            qi = qi1
            print("Part 4")
        elif resul[0][0] == 4:
            pi = Pi0
            qi = Qi0
            print("Part 5")
        else:
            pi = parti1.posCaraMed[caraA]
            qi = parti2.posCaraMed[caraB]
            print("Part 6")
            
        
        
        
        
        '''
        distAux = 100
        dista = 100
        i = 0
        while dista == distAux:
            pi, caraA = f.SL(posA, Q0, parti1, sliRotaBZ.value)
            qi, caraB = f.SL(posB, pi, parti2, 631)
            
            distAux = dista
            dista = f.distancia(pi, qi)
            i = i + 1
        
        distanciasFinales = np.array([1000, f.distancia(pi, qi), f.distancia(parti1.posCaraMed[caraA],parti2.posCaraMed[caraB]) ])
        
        print("-----------------------------------------")
        print("Vert1 = ", numVertA)
        print("Vert2 = ", numVertB)
        print("-----------------------------------------")
        
        if ariAri[0][0] != 100 and ariAri[1][0] != 100:
            distanciasFinales[0] =  f.distancia(ariAri[0], ariAri[1])
        
        resul = np.where(distanciasFinales == np.amin(distanciasFinales))
        
        
        print("///////////////////////////////////////////////////")
        if resul[0][0] == 0:
            pi = ariAri[0]
            qi = ariAri[1]
            print("5")
        elif resul[0][0] == 2:
            pi = parti1.posCaraMed[caraA]
            qi = parti2.posCaraMed[caraB]
            print("6")
        else:
            print("7")
        print("///////////////////////////////////////////////////")
        '''
        
        
        #actualizamos los graficos que se muestran por pantalla
        for i in range(5):
            graSL.SL[i].visible = True
        graSL.SL[0].pos = v.vector(qi[0],qi[1],qi[2])
        graSL.SL[1].pos = v.vector(pi[0],pi[1],pi[2])
        graSL.SL[2].pos = v.vector(qi[0],qi[1]+0.3,qi[2]+0.3)
        graSL.SL[3].pos = v.vector(pi[0],pi[1]+0.3,pi[2]+0.3)
        graSL.SL[4].pos = v.vector(pi[0],pi[1],pi[2])
        graSL.SL[4].axis = v.vector(qi[0],qi[1],qi[2]) - v.vector(pi[0],pi[1],pi[2])
        
        
    
        part[1].pos = v.vector(posB[0],posB[1],posB[2])
        VCC.axis = part[1].pos - part[0].pos
        nompart[1].pos = v.vector(posB[0] + 0.1, posB[1] + 0.1, posB[2] + 0.1)
            
        
        pe0.pos = v.vector(P0[0],P0[1],P0[2])
        qu0.pos = v.vector(Q0[0],Q0[1],Q0[2])
    
        
        '''
        print("Distancia P0 qi1 = ", f.distancia(P0,qi1))
        print("Distancia Q0 pi1 = ", f.distancia(Q0,pi1))
        print("Distancia P0 Q0 = ", f.distancia(P0,Q0))
        print("Distancia pi1 qi1 = ", f.distancia(pi1,qi1))
        print("-------------------\n\n\n")
        print("Distancia |qi pi| = ", f.distancia(qi, pi))
        print("\n\n\n")
        
        algo.pos = v.vector(a[0],a[1],a[2])
        algo3.pos = v.vector(pi1[0],pi1[1],pi1[2])
        algo2.pos = v.vector(a[0],a[1],a[2])
        algo2.axis = v.vector(qi1[0],qi1[1],qi1[2]) - v.vector(a[0],a[1],a[2])
        '''
        
        puMedio = f.punAleaAris(np.array([pi, qi]), 0.5)
        '''
        pbp.pos = v.vector(puMedio[0], puMedio[1], puMedio[2])
        pbp.axis = v.vector(qi[0], qi[1], qi[2]) - v.vector(puMedio[0], puMedio[1], puMedio[2])
        pbp.length = 0.01
        '''
    
        #actualizamos el plano del SL
        dNormal, d = f.creaPlano(puMedio, qi)
        
        #actualizamos el plano de centroide centroide
        punMedio = [(posA[0]+posB[0])/2,(posA[1]+posB[1])/2,(posA[2]+posB[2])/2]
       
        '''
        pbp.pos = v.vector(punMedio[0], punMedio[1], punMedio[2])
        pbp.axis = v.vector(posA[0], posA[1], posA[2]) - v.vector(puMedio[0], puMedio[1], puMedio[2])
        pbp.length = 0.01
        '''
        
        distSL(f.distancia(pi, qi))
        
        dNormal2, d2 = f.creaPlano(punMedio, posB)
        
        valMovi0 = valMovi
    
    valMovi = np.array([sliRotaAX.value, sliRotaBX.value, sliRotaAY.value, sliRotaBY.value, sliRotaAZ.value, sliRotaBZ.value, sliDistancia.value])





