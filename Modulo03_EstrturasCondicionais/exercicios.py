# 2) - 

sexo = input("Digite seu sexo [M | F]: ")
altura = float(input("Digite sua altura: "))

if sexo.upper() == "F":
    peso = (72.7 * altura) - 58
    print("Seu peso ideal é {:.2f} kg".format(peso))
elif sexo.upper() == "M":
    peso = (62.2 * altura) - 44.7
    print("Seu peso ideal é {:.2f} kg".format(peso))
else:
    print("Opção de sexo invalida.")