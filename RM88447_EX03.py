print("====Apuração de Votos - Melhor dia para Lives====")

segunda = int(input("Insira os votos da Segunda-feira: "))  # variável dia
terca = int(input("Insira os votos da Terça-feira: ")) # variável dia
quarta = int(input("Insira os votos da Quarta-feira: ")) # variável dia
quinta = int(input("Insira os votos da Quinta-feira: ")) # variável dia
sexta = int(input("Insira os votos da Sexta-feira: ")) # variável dia

maior_votos = segunda # variável auxiliar para comparar votos
maior_dia = "Segunda-Feira" # variável auxiliar para atribuir ao dia com mais votos

if (terca > maior_votos):
    maior_votos = terca
    maior_dia = "Terça-Feira"
if (quarta > maior_votos):
    maior_votos = quarta
    maior_dia = "Quarta-Feira"
if (quinta > maior_votos):
    maior_votos = quinta
    maior_dia = "Quinta-Feira"
if (sexta > maior_votos):
    maior_votos = sexta
    maior_dia = "Sexta-Feira"
else:
    print("====FIM DA APURAÇÃO====")

print("O dia mais votado foi {} com {} votos".format(maior_dia, maior_votos)) # impressão do resultado
 #Não tratei empates, se houver empate o primeiro ganha.

