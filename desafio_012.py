# Leia o preço de um produto e mostre seu novo preço com 5% de desconto

prod = float(input("Digite o preço do produto: R$ "))
desc = prod * 0.05
novo = prod - desc

print(f"O produto saiu de R$ {prod} para R$ {novo} com o desconto de 5%")