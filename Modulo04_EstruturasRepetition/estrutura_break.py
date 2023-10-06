# Programando um break e continue
# NOTA: na estrutura (for) é necessario especificar quatas vezes ela vai rodar,
# já na estrutura (while), não é necessario saber quantas vezes aquela estrutura vai se repitir,
# uma vez que é possivel controlar
print("COVID-19")

suspeitos = 0
while True:
    tosse = int(input("Tosse? \n1. Sim \n2. Não \nRespo.: ")) # o \n significa uma quebra de linhas
    febre = int(input("Febre? \n1. Sim \n2. Não \nRespo.: "))
    resp = int(input("Dificuldade de respirar? \n1. Sim \n2. Não \nRespo.: "))

    if tosse == 1 and febre == 1 and resp == 1:
        suspeitos += 1 # suspeitos = suspeitos + 1
    resp = input("Ainda há pacientes  a serem atendidos [S|N]? ")
    if resp.upper() == "N":
        break    

print("Suspeitos de COVID-19: {}".format(suspeitos))        