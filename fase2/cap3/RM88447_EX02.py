print("====Calculo do total e média de transações financeiras====")

valor_total = 0
transacoes = int(input("Quantos transações financeira fez hoje? "))

for x in range(1,transacoes+1):
    valor = float(input("Qual o valor da transação {}? ".format(x)))
    valor_total = valor_total + valor
media = valor_total/transacoes

print("Você gastou um total $ {:,.2f}, com uma média de $ {:,.2f} em cada transação.".format(valor_total, media))