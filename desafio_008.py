# Leia o valor em metros e o exiba convertido em centimetros e milimetros

valor = float(input("Digite o valor em metros: "))
cm = valor * 100
mm = valor * 1000

print(f"O valor {valor} em metros corresponde a {cm} centimetros e {mm} em milimetros")