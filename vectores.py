import random
from math import sqrt

x1= random.randint(-10,10)
y1=random.randint(-10,10)

x2= random.randint(-10,10)
y2=random.randint(-10,10)

print("El vector A es: (", x1, ",", y1, ")")
print("El vector B es: (", x2, ",", y2, ")")
#Suma
Xsuma= x1+x2
Ysuma= y1+y2
print("El vector resultante de la suma de A mas B es: (",Xsuma, ",", Ysuma,")")

#Resta
Xresta= x1-x2
Yresta= y1-y2
print("El vector resultante de la resta de A menos B es: (",Xresta, ",", Yresta,")")

#Normalizar
productoA= x1**2+y1**2
productoB= x2**2+y2**2

raizA= sqrt(productoA)
raizB= sqrt(productoB)

XnormalA= x1/raizA
YnormalA= y1/raizA

XnormalB= x2/raizB
YnormalB= y2/raizB

print("El vector A normalizado es: (", XnormalA, ",", YnormalA,")")
print("El vector B normalizado es: (", XnormalB, ",", YnormalB,")")

