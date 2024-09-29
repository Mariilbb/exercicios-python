# Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e calcule sua hipotenusa

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hip = (co ** 2 + ca ** 2) ** (1/2)

print("A hipotenusa vai medir: {:.2f}" .format(hip))

# OU

from math import hypot

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hip = hypot(co, ca)

print("A hipotenusa vai medir: {:.2f}" .format(hip))

