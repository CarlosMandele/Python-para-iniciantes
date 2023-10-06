# Estrutura de respetição: programando um laço com BREAK
rapazes_maiores = 0
soma_idade_meninas = 0
meninas = 0
while True:
    sexo = input("Sexo [M|F]: ")
    idade = input("Idade: ")
    if idade < 0:
        break

    if sexo.upper() == "M":
        if idade > 18:
            rapazes_maiores += 1
    elif sexo.upper() == "F":
        soma_idade_meninas += idade
        meninas += 1
    else:
        print("Opção de sexo inválida.")

media = 0       
if meninas > 0:
   media = soma_idade_meninas / meninas

print("Rapazes acima de 18 anos: {}".format(rapazes_maiores))
print("Média de idade das meninas: {}".format(media))                   