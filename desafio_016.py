# Leia um número real qualquer e mostre na tela sua porção inteira

from math import trunc

num = float(input("Digite um número real: "))
inteiro = trunc(num)

print(f"O número {num} arredondado fica: {inteiro}")