print("====Calculadora de IMC-HealthTrack====")

peso = float(input("Insira a seu peso: ")) # variável peso
altura = float(input("Insira a sua altura: ")) # variável altura

imc = peso/(altura**2) # calculo do IMC

if imc < 16.00:
    print("Vc tem IMC de {:.2f} e está com Baixo peso Grau III".format(imc))
elif (imc >= 16.00 and imc <= 16.99):
    print("Vc tem IMC de {:.2f} e está com Baixo peso Grau II".format(imc))
elif imc >= 17.00 and imc <= 18.49:
    print("Vc tem IMC de {:.2f} e está com Baixo peso Grau I".format(imc))
elif imc >= 18.50 and imc <= 24.99:
    print("Vc tem IMC de {:.2f} e está com Peso ideal".format(imc))
elif imc >= 25.00 and imc <= 29.99:
    print("Vc tem IMC de {:.2f} e está com Sobrepeso".format(imc))
elif imc >= 30.00 and imc <= 34.99:
    print("Vc tem IMC de {:.2f} e está com Obesidade Grau I".format(imc))
elif imc >= 35.00 and imc <= 39.99:
    print("Vc tem IMC de {:.2f} e está com Obesidade Grau II".format(imc))
else:
    print("Vc tem IMC de {:.2f} e está com Obesidade Grau III".format(imc))