menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_depositado = float(input("Digite o valor a ser depositado: "))
        if valor_depositado <= 0:
            print("Digite um valor válido")
        saldo += valor_depositado
        extrato += f"Foi Depositado R$ {valor_depositado:.2f}\n"
        
    elif opcao == "s":
        saque = float(input("Digite o valor a ser sacado: "))

        if numero_saques >= LIMITE_SAQUES:
           print ("\nVocê excedeu o número de saques hoje. Poderá efetuar novos saques amanhã")
        elif saldo < saque:
            print("\nVocê não tem saldo suficiente")
        elif saque > limite:
            print("\nVocê só pode sacar no máximo R$ 500,00 por vez")
        else:        
            saldo -= saque
            numero_saques += 1  
            extrato += f"Foi Sacado R$ {saque:.2f}\n"                            

    elif opcao == "e":
        print("############################# EXTRATO ###########################\n")
        print("Não houve movimentações na sua conta" if not extrato else extrato)
        print(f"Seu saldo em conta é: R$ {saldo:.2f}\n")
        print("###################################################################")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")