# 1)- Escreva um programa que leia duas notas de um aluno de programação.
# Em seguida, a média ponderada, com pesos 2 e 3, respectivamente, deve ser calculada.
# Por fim, o programa deve imprimir a média obtida.

nota1 = float(input("Digite a primeira nota: ")) # 7
nota2 = float(input("Digite a segunda nota: ")) # 7

media = (nota1 * 2 + nota2 * 3) / 5

print("Média = {: .2f}".format(media))