# Programando um for
print("COVID-19")

suspeitos = 0
num_pacientes = int(input("Informe a quantidade de pacientes: "))
for x in range(num_pacientes):
    tosse = int(input("Tosse? \n1. Sim \n2. Não \nRespo.: ")) # o \n significa uma quebra de linhas
    febre = int(input("Febre? \n1. Sim \n2. Não \nRespo.: "))
    resp = int(input("Dificuldade de respirar? \n1. Sim \n2. Não \nRespo.: "))

    if tosse == 1 and febre == 1 and resp == 1:
        suspeitos += 1 # suspeitos = suspeitos + 1

print("Suspeitos de COVID-19: {}".format(suspeitos))        