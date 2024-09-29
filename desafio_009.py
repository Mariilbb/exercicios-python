# Leia um numero inteiro e mostre a sua tabuada

num = int(input("Digite um numero: "))
num1 = num * 1
num2 = num * 2
num3 = num * 3
num4 = num * 4
num5 = num * 5
num6 = num * 6
num7 = num * 7
num8 = num * 8
num9 = num * 9
num10 = num * 10

print(f"{num} X 1 = {num1}")
print(f"{num} X 2 = {num2}")
print(f"{num} X 3 = {num3}")
print(f"{num} X 4 = {num4}")
print(f"{num} X 5 = {num5}")
print(f"{num} X 6 = {num6}")
print(f"{num} X 7 = {num7}")
print(f"{num} X 8 = {num8}")
print(f"{num} X 9 = {num9}")
print(f"{num} X 10 = {num10}")

# OU

num = int(input("Digite um número: "))

print("{} X {:2} = {}".format(num, 1, num+1))
print("{} X {:2} = {}".format(num, 2, num+1))
print("{} X {:2} = {}".format(num, 3, num+1))
print("{} X {:2} = {}".format(num, 4, num+1))
print("{} X {:2} = {}".format(num, 5, num+1))
print("{} X {:2} = {}".format(num, 6, num+1))
print("{} X {:2} = {}".format(num, 7, num+1))
print("{} X {:2} = {}".format(num, 8, num+1))
print("{} X {:2} = {}".format(num, 9, num+1))
print("{} X {:2} = {}".format(num, 10, num+1))