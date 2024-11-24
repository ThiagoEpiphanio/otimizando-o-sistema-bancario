
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("\nVocê excedeu o número de saques hoje. Poderá efetuar novos saques amanhã.")
    elif saldo < valor:
        print("\nVocê não tem saldo suficiente.")
    elif valor > limite:
        print("\nVocê só pode sacar no máximo R$ 500,00 por vez.")
    else:        
        saldo -= valor
        numero_saques += 1  
        extrato += f"Foi Sacado R$ {valor:.2f}\n"                             
    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("Digite um valor válido.")
    else:
        saldo += valor
        extrato += f"Foi Depositado R$ {valor:.2f}\n"
    return saldo, extrato


def visualizar_extrato(saldo, *, extrato):
    print("############################# EXTRATO ###########################\n")
    print("Não houve movimentações na sua conta" if not extrato else extrato)
    print(f"Seu saldo em conta é: R$ {saldo:.2f}\n")
    print("###################################################################")


def cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    cpf = cpf.replace("-", "").replace(".", "")
    if any(u['cpf'] == cpf for u in usuarios):
        print("Erro: Já existe um usuário com esse CPF.")
        return usuarios
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print(f"Usuário {nome} cadastrado com sucesso!")
    return usuarios


def cadastrar_conta(usuarios, contas, usuario_cpf):
    agencia = "0001"
    numero_conta = len(contas) + 1
    usuario = next((u for u in usuarios if u['cpf'] == usuario_cpf), None)
    
    if usuario:
        contas.append({
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print(f"Conta {numero_conta} cadastrada com sucesso para o usuário {usuario['nome']}!")
    else:
        print("Erro: Usuário não encontrado.")
    return contas


def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []  
    contas = [] 

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar Usuário
    [c] Cadastrar Conta
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor_depositado = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor_depositado, extrato)
            
        elif opcao == "s":
            saque = float(input("Digite o valor a ser sacado: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            
        elif opcao == "e":
            visualizar_extrato(saldo, extrato=extrato)
            
        elif opcao == "u":
            nome = input("Nome: ")
            data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, número, bairro, cidade/sigla estado): ")
            usuarios = cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco)
            
        elif opcao == "c":
            usuario_cpf = input("Digite o CPF do usuário para vincular a conta: ")
            contas = cadastrar_conta(usuarios, contas, usuario_cpf)
            
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()