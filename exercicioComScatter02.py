import math
from random import randint
import numpy as np
import matplotlib.pyplot as plt

##1. Desenvolva uma aplicação para geração dos pontos de um circuito automotivo fechado, 
# a partir de pelo menos 4 curvas de Bézier ou Hermite interligadas entre si, de modo que a última curva termine se conectando a primeira. 
# Defina os valores diretamente no código/leia pelo teclado), e em seguida aplique o algoritmo escolhido 
# (Bézier ou Hermite), apresentando os pontos resultantes do circuito gerado na tela. 

##1.0 ponto extra para quem conseguir gerar circuitos aleatórios com curvas suaves.

##Você pode testar os resultados na ferramenta online Desmos: https://www.desmos.com/

p1x = 0
p1y = -10
p3x = -10
p3y = 0
p5x = 0
p5y = 12
p7x = 14
p7y = 0

p2x = -10
p2y = 0
p4x = 0
p4y = 12
p6x = 14
p6y = 0
p8x = 0
p8y = -10

m1x = randint(-20,1) #-20
m1y = randint(-15 ,1) #-15
m3x = randint(5,30) #5
m3y = randint(5,30) #5
m5x = randint(1,30) #1
m5y = randint(30,-10) #30
m7x = randint(20,-10) #20
m7y = randint(-5,20) #-5

m2x = 15
m2y = 5
m4x = -5
m4y = 20
m6x = 1
m6y = 1
m8x = 2
m8y = -15

t = 0.0

inc = 0.01

while t <= 1.0:

    parte1 = 2*t**3-3*t**2+1
    parte2 = t**3-2*t**2+t
    parte3 = -2*t**3+3*t**2
    parte4 = t**3-t**2

    curvax1 = (parte1)*p1x + (parte2)*m1x + (parte3)*p2x + (parte4)*m2x
    curvay1 = (parte1)*p1y + (parte2)*m1y + (parte3)*p2y + (parte4)*m2y

    curvax2 = (parte1)*p3x + (parte2)*m3x + (parte3)*p4x + (parte4)*m4x
    curvay2 = (parte1)*p3y + (parte2)*m3y + (parte3)*p4y + (parte4)*m4y

    curvax3 = (parte1)*p5x + (parte2)*m5x + (parte3)*p6x + (parte4)*m6x
    curvay3 = (parte1)*p5y + (parte2)*m5y + (parte3)*p6y + (parte4)*m6y

    curvax4 = (parte1)*p7x + (parte2)*m8x + (parte3)*p8x + (parte4)*m8x
    curvay4 = (parte1)*p7y + (parte2)*m8y + (parte3)*p8y + (parte4)*m8y

    print("(",round(curvax1,2),",",round(curvay1,2),")")
    plt.scatter(curvax1, curvay1)

    print("(",round(curvax2,2),",",round(curvay2,2),")")
    plt.scatter(curvax2, curvay2)

    print("(",round(curvax3,2),",",round(curvay3,2),")")
    plt.scatter(curvax3, curvay3)

    print("(",round(curvax4,2),",",round(curvay4,2),")")
    plt.scatter(curvax4, curvay4)
    
    t+=inc
    


plt.grid()
plt.show()