# Leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

sal = float(input("Digite seu salario: R$ "))
aum = sal * 0.15
novo = sal + aum

print(f"Seu novo salario com o aumento de 15% ficou em R$ {novo}")