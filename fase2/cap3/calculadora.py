print("====Calculo do alcance anuncio====")

valor = 0
qVi = 0
qCl = 0
qCom = 0
qVi = 0
qTo = 0

valor = float(input("Qual o valor do investimento?"))

qVi = 30 * valor #calcula quant inicial a cada R$ investido em visualizações
qCl = (qVi * 12) / 100 #calcula quant de cliques a cada qVi
qCom = (qCl * 3) / 20 #calcula quant compartilhamento a cada qCl
qViCl = qCom * 40 #calcula quant visualização a cada qCl
qTo = qVi + (qViCl * qViCl * qViCl * qViCl) #calcula quant total somando qVi mais qViCl, multiplicado por ele mesmo 4X

print("Você investiu $ {:,.2f}, com um retorno {:.2f} em visualizações em cada anuncio.".format(valor, qTo))