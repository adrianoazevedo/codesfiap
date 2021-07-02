print("====Calculadora de Bonus sobre o faturamento====")
print("Tipos de Assinatura:")
print("BASIC")
print("SILVER")
print("GOLD")
print("PLATINUM")

nivel = input("Insira o tipo de assinatura: ") # variável nivel
faturamento = float(input("Insira faturamento anual: ")) # variável faturamento

if nivel.upper() == "BASIC":
    bonus = faturamento*0.30
elif nivel.upper() == "SILVER":
    bonus = faturamento*0.20
elif nivel.upper() == "GOLD":
    bonus = faturamento*0.10
elif nivel.upper() == "PLATINUM":
    bonus = faturamento*0.05
else:
    nivel = "INVALIDO"
    faturamento = 0
    bonus = 0
    print("Vc não digitou um Nível Válido")

print("Como vc é Nível {}, faturou $ {:,.2f} e deve pagar de bonus $ {:,.2f}".format(nivel.upper(), faturamento, bonus))
