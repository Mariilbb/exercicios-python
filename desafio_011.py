# Leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessaria para pintá-la
# Sabendo que cada litro de tinta pinta uma área de 2m²

larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))
area = larg * alt
tinta = area / 2

print(f"A área da parede é de {area} m²")
print(f"A quantidade de tinta necessária para pintar a parede será {tinta} litros")