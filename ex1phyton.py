import math
import numpy


matT = numpy.array ([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])

print("Matriz: \n", matT)

while True:
    print("Escolha uma opção: ")

    print("1. Translação")
    print("2. Rotação")
    print("3. Escala")
    print("4. Próxima etapa")

    op = input("Escolha:")
    op = int(op)

    if op == 1:
        Tx = input ('Tx: ')
        Tx = float(Tx)

        Ty = input ('Ty: ')
        Ty = float(Ty)

        matTran = numpy.array ([[1, 0, Tx],
                                [0, 1, Ty],
                                [0, 0, 1]])
        matT = matTran.dot(matT)      
        print(matT)
    
    elif op == 2:

        angulo = input ('Angulo: ')
        angulo = float(angulo)

        anguloRad = math.radians(angulo)

        matR = numpy.array ([[math.cos(anguloRad), -math.sin(anguloRad), 0],
                           [math.sin(anguloRad), math.cos(anguloRad), 0],
                           [0, 0, 1]])
        
        matT = matR.dot(matT)
        matT = numpy.round_(matT, 2)
        print(matT)

    elif op == 3:
        Sx = input ('Sx: ')
        Sx = float(Sx)
        Sy = input ('Sy:')
        Sy = float(Sy)

        matE = numpy.array ([[Sx, 0, 0],
                           [0, Sy, 0],
                           [0, 0, 1]])
        matT = matE.dot(matT) 
        print(matT)

    elif op == 4:
        False
        break

print("Digite os pontos: ")
while True:
    Xo = input ('X:')
    Xo = float(Xo)
    Yo = input ('Y:')
    Yo = float(Yo)

    pontoV = numpy.array([Xo, Yo, 1])
    vetorR = matT.dot(pontoV)
    print(vetorR)