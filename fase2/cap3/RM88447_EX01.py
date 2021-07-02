print("====Calculo de total de calorias num dia====")

calorias_total = 0
alimentos = int(input("Quantos alimentos consumiu hoje? "))

for x in range(1,alimentos+1):
    calorias = int(input("Quantas calorias tem o alimento {}? ".format(x)))
    calorias_total = calorias_total + calorias

print("Você consumiu {} alimentos, totalizando {} calorias.".format(alimentos, calorias_total))