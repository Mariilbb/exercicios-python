# Leia um ângulo qualquer e mostre seu valor do seno, cosseno e tangente

import math

angulo = int(input("Digite o ângulo: "))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print("O seno do ângulo {:.2f} é: {:.2f}" .format(angulo, seno))
print("O cosseno do ângulo {:.2f} é: {:.2f}" .format(angulo, cos))
print("A tangente do ângulo {:.2f} é: {:.2f}" .format(angulo, tan))