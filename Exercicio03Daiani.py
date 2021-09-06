import math
import numpy as np
import matplotlib.pyplot as plt
 
#Foi feito a escolha de piramide
 
p1 = np.array([0.0 , 1.0 , 0.0, 1.0])
p2 = np.array([1.0 , 0.4 , -0.5, 1.0])
p3 = np.array([0.0 , -1.0 , 1.0, 1.0])
p4 = np.array([-0.7 , 0.0 , 0.0, 1.0])
p5 = np.array([0.2 , -0.2 , 0.0, 1.0])
 
Transformacao = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])
 
matrizVisualizacao = np.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, -4],
                                [0, 0, 0, 1]])
 
matrizProjecao = np.array([[1/1*math.tan(60/2),0,0,0],
                            [0,1/math.tan(60/2),0,0],
                            [0,0,(100+0.1)/(0.1-100),(2*100*0.1)/(0.1-100)],
                            [0,0,-1,0]])
 
xminw = -1
yminw = -1
xmaxw = 1
ymaxw = 1
 
xminv = 0
xmaxv = 500
yminv = 0
ymaxv = 500
 
while True:
 
    print("Escolha uma opção: ") 
 
    print("1. Manipular o objeto")
    print("2. Manipular a câmera")
    print("3. Modificar projeção")
    print("4. Modificar mapeamento")
    print("5. Visualizar objeto")
 
    op = input("Escolha:")
    op = int(op)
 
    if op == 1:
 
        print("Escolha o que deseja manipular: ")
 
        print("1 - Translação")
        print("2 - Escala")
        print("3 - Rotação em X")
        print("4 - Rotação em Y")
        print("5 - Rotação em Z")
        print("6 - Voltar")
 
        opi = input("Escolha:")
        opi = int(opi)
 
        if opi == 1:
            Tx = input ('Tx: ')
            Tx = float(Tx)
 
            Ty = input ('Ty: ')
            Ty = float(Ty)
 
            Tz = input ('Tz: ')
            Tz = float(Tz)
 
            matTran = np.array ([[1, 0, 0, Tx],
                                [0, 1, 0, Ty],
                                [0, 0, 1, Tz],
                                [0, 0, 0, 1]])
            Transformacao = matTran.dot(Transformacao) 
                
        if opi == 2:
            Sx = input ('Sx: ')
            Sx = float(Sx)
            Sy = input ('Sy: ')
            Sy = float(Sy)
            Sz = input ('Sz: ')
            Sz = float (Sz)
 
            matEscala = np.array ([[Sx, 0, 0, 0],
                                    [0, Sy, 0, 0],
                                    [0, 0, Sz, 0],
                                    [0, 0, 0, 1]])
            Transformacao = matEscala.dot(Transformacao) 
 
        if opi == 3:
            angulo = input ('Angulo: ')
            angulo = float(angulo)
            anguloRad = math.radians(angulo)
            rotacaoX = np.array([[1, 0, 0, 0],
                                [0, math.cos(angulo), -math.sin(angulo), 0],
                                [0, math.sin(angulo), math.cos(angulo), 0],
                                [0,0,0,1]])
            Transformacao = rotacaoX.dot(Transformacao) 
 
        if opi == 4:
            angulo = input ('Angulo: ')
            angulo = float(angulo)
            anguloRad = math.radians(angulo)
            rotacaoY = np.array([[math.cos(angulo),0,math.sin(angulo),0],
                                [0,1,0,0],
                                [-math.sin(angulo),0,math.cos(angulo),0],
                                [0,0,0,1]])
            Transformacao = rotacaoY.dot(Transformacao) 
 
        if opi == 5:
            angulo = input ('Angulo: ')
            angulo = float(angulo)
            anguloRad = math.radians(angulo)
            rotacaoZ = np.array([[math.cos(angulo), -math.sin(angulo), 0, 0],
                                [math.sin(angulo), math.cos(angulo),0,0],
                                [0, 0, 1, 0],
                                [0,0,0,1]])
            Transformacao = rotacaoZ.dot(Transformacao) 
 
    if op == 2:
 
        print("1 - Translação")
        print("2 - Rotação em X")
        print("3 - Rotação em Y")
        print("4 - Rotação em Z")
 
        opi = input("Escolha:")
        opi = int(opi)
 
        if opi == 1:
 
            cameraX = input ('Camera X: ')
            cameraX = float(cameraX)
            cameraY = input ('Camera Y: ')
            cameraY = float(cameraY)
            cameraZ = input ('Camera Z: ')
            cameraZ = float(cameraZ)
 
            translacaoCamera = np.array([[1, 0, 0, -cameraX],
                                        [0, 1, 0, -cameraY],
                                        [0, 0, 1, -cameraZ],
                                        [0, 0, 0, 1]])
            matrizVisualizacao = translacaoCamera.dot(matrizVisualizacao)
 
        if opi == 2:
            anguloCamera = input ('Angulo Da camera em X')
            anguloCamera = int(anguloCamera)
 
            anguloCamera = math.radians(anguloCamera)
 
            rotacaoCamera = np.array([[1, 0, 0, 0],
                                      [0, math.cos(-anguloCamera), -math.sin(-anguloCamera), 0],
                                      [math.sin(-anguloCamera), 0, math.cos(-anguloCamera), 0],
                                      [0, 0, 0, 1]])
            matrizVisualizacao = rotacaoCamera.dot(matrizVisualizacao)
 
        if opi == 3:
            anguloCamera = input ('Angulo Da camera em Y')
            anguloCamera = int(anguloCamera)
 
            anguloCamera = math.radians(anguloCamera)
 
            rotacaoCamera = np.array([[math.cos(-anguloCamera), 0, math.sin(-anguloCamera), 0],
                                      [0, 1, 0, 0],
                                      [-math.sin(-anguloCamera), 0, math.cos(-anguloCamera), 0],
                                      [0, 0, 0, 1]])
            matrizVisualizacao = rotacaoCamera.dot(matrizVisualizacao)
 
        if opi == 4:
            anguloCamera = input ('Angulo Da camera em Z')
            anguloCamera = int(anguloCamera)
 
            anguloCamera = math.radians(anguloCamera)
 
            rotacaoCamera = np.array([[math.cos(-anguloCamera), -math.sin(-anguloCamera), 0, 0],
                                      [math.sin(-anguloCamera), math.cos(-anguloCamera), 0, 0],
                                      [0, 0, 1, 0],
                                      [0, 0, 0, 1]])
            matrizVisualizacao = rotacaoCamera.dot(matrizVisualizacao)
 
    if op == 3:
        print("1 - Projeção perspectiva")
        print("2 - Projeção paralela")
        
 
        opi = input("Escolha:")
        opi = int(opi)
 
        if opi == 1:
            angulo = input ('Angulo: ')
            angulo = float(angulo)
            aspecto = input ('Largura: ')
            aspecto = float(aspecto)
            zNear = input ('Corte frontal:')
            zNear = float(zNear)
            zFar = input('Corte trazeiro: ')
            zFar = float(zFar)
 
            fovy = math.radians(angulo)
 
            matrizProjecao = np.array([[1/aspecto*math.tan(fovy/2),0,0,0],
                                        [0,1/math.tan(fovy/2),0,0],
                                        [0,0,(zFar+zNear)/(zNear-zFar),(2*zFar*zNear)/(zNear-zFar)],
                                        [0,0,-1,0]])
            
        elif opi == 2:
 
            emX = input ('Valor em X: ')
            emX = float(emX)
            emY = input ('Valor em Y: ')
            emY = float(emY)
            emZ = input ('Valor em Z: ')
            emZ = float(emZ)
 
            matrizProjecao = np.array([[2/emX-emX,0,0,-(emX+emX/emX-emX)],
                                        [0,2/emY-emY,0,-(emY+emY/emY-emY)],
                                        [0,0,-(2/emZ-emZ),-(emZ+emZ/emZ-emZ)],
                                        [0,0,0,1]])
 
    if op == 4:
        print("1 - Window")
        print("2 - Viewport")
 
        opi = input("Escolha:")
        opi = int(opi)
 
        if opi == 1: #le pelo teclado os valores abaixo
            xminw = input ('Valor do X minimo: ')
            xminw = float(xminw)
            yminw = input ('Valor do Y minimo: ')
            yminw = float(yminw)
            
            xmaxw = input ('Valor do X maximo: ')
            xmaxw = float(xmaxw)
            ymaxw = input ('Valor do Y maximo: ')
            ymaxw = float(ymaxw)
           
 
        elif opi == 2: #le pelo teclado os valores abaixo

            xminv = input ('Valor do X minimo: ')
            xminv = float(xminv)
            yminv = input ('Valor do Y minimo: ')
            yminv = float(yminv)

            xmaxv = input ('Valor do X maximo: ')
            xmaxv = float(xmaxv)
            ymaxv = input ('Valor do Y maximo: ')
            ymaxv = float(ymaxv)
           
    if op == 5:
        
        p1u = Transformacao.dot(p1)
        p2u = Transformacao.dot(p2)
        p3u = Transformacao.dot(p3)
        p4u = Transformacao.dot(p4)
        p5u = Transformacao.dot(p5)
 
        print("\nUniverso")
        print(p1u)
        print(p2u)
        print(p3u)
        print(p4u)
        print(p5u)
 
        p1v = matrizVisualizacao.dot(p1u)
        p2v = matrizVisualizacao.dot(p2u)
        p3v = matrizVisualizacao.dot(p3u)
        p4v = matrizVisualizacao.dot(p4u)
        p5v = matrizVisualizacao.dot(p5u)
 
        print("\nCamera")
        print(p1v)
        print(p2v)
        print(p3v)
        print(p4v)
        print(p5v)
 
        p1p = matrizProjecao.dot(p1v)
        p2p = matrizProjecao.dot(p2v)
        p3p = matrizProjecao.dot(p3v)
        p4p = matrizProjecao.dot(p4v)
        p5p = matrizProjecao.dot(p5v)
 
        p1p = p1p/p1p[3]
        p2p = p2p/p2p[3]
        p3p = p3p/p3p[3]
        p4p = p4p/p4p[3]
        p5p = p5p/p5p[3]
        
        print("\nProjecao")
        print(p1p)
        print(p2p)
        print(p3p)
        print(p4p)
        print(p5p)
        
        print("\nVisualização")
        xv1 = (((p1p[0]-xminw)*(xmaxv-xminv))/(xmaxw-xminw))+xminv
        yv1 = (((p1p[1]-yminw)*(ymaxv-yminv))/(ymaxw-yminw))+yminv
        print(xv1,",",yv1)
        xv2 = (((p2p[0]-xminw)*(xmaxv-xminv))/(xmaxw-xminw))+xminv
        yv2 = (((p2p[1]-yminw)*(ymaxv-yminv))/(ymaxw-yminw))+yminv
        print(xv2,",",yv2)
        xv3 = (((p3p[0]-xminw)*(xmaxv-xminv))/(xmaxw-xminw))+xminv
        yv3 = (((p3p[1]-yminw)*(ymaxv-yminv))/(ymaxw-yminw))+yminv
        print(xv3,",",yv3)
        xv4 = (((p4p[0]-xminw)*(xmaxv-xminv))/(xmaxw-xminw))+xminv
        yv4 = (((p4p[1]-yminw)*(ymaxv-yminv))/(ymaxw-yminw))+yminv
        print(xv4,",",yv4)
        xv5 = (((p5p[0]-xminw)*(xmaxv-xminv))/(xmaxw-xminw))+xminv
        yv5 = (((p5p[1]-yminw)*(ymaxv-yminv))/(ymaxw-yminw))+yminv
        print(xv5,",",yv5)
        
        plt.scatter(xv1, yv1) 
        plt.scatter(xv2, yv2) 
        plt.scatter(xv3, yv3) 
        plt.scatter(xv4, yv4) 
        plt.scatter(xv5, yv5) 
        
        plt.plot([xv1, xv3], [yv1, yv3]) 
        plt.plot([xv1, xv2], [yv1, yv2]) 
        plt.plot([xv2, xv3], [yv2, yv3]) 
        plt.plot([xv3, xv4], [yv3, yv4]) 
        plt.plot([xv4, xv1], [yv4, yv1])  
        plt.plot([xv3, xv5], [yv3, yv5])  
        plt.plot([xv4, xv5], [yv4, yv5])
        plt.plot([xv5, xv2], [yv5, yv2])
        plt.show()