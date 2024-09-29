# Converta uma temperatura de °C para °F
# C°/5 = (°F-32)/9

cel = float(input("Digite a temperatura que deseja converter: °C"))
far = (cel * 1.8) + 32

print("A temperatura {:.2f} °C fica {:.2f} em °F".format(cel, far))

# OU

cel = float(input("Digite a temperatura que deseja converter: °C"))
far = 9 * cel / 5 + 32

print("A temperatura {:.2f} °C fica {:.2f} em °F".format(cel, far))


