print("====Verifica se numero faz parte da sequencias Fibonacci")

n = int(input("Que numero inteiro deseja encontrar? "))

ultimo = 1
penultimo = 1

if ((n == 1) or (n == 2)):
    print("Ação bem sucedida!")
elif n >= 3:
    while ultimo < n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        termo += 1
        #print(ultimo) descomente se quiser imprimir a sequencia
        if n == ultimo:
            print("Ação bem sucedida!")
    if ultimo != n:
        print("A ação falhou...")