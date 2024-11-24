1. Separar as funções existentes. Criar funções para:
   
    1.1 Saque
        Deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
        Sugestão retorno: saldo e extrato.

    1.2 Depósito
        Deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato.
        Sugestão retorno: saldo e extrato.

    1.3 Visualizar Extrato
        Deve receber os argumentos por posição e nome. Argumentos posicionais: saldo, argumentos nomeados: extrato.

2. Criar novas funções. Criar funções para:
   
    2.1 Cadastrar Usuário (Cliente)
        Armazenar usuários em uma lista (Nome, data nascimento, cpf, endereço (logradouro, número, bairro, cidade/sigla estado))
        Deve ser armazenado somente os numeros do cpf (string, sem ponto e sem hifen). Não pode cadastrar 2 usuários com o mesmo cpf (mensagem erro caso repita)

    2.2 Cadastrar Conta Bancária (Vincular com o Usuário)
        Cadastrar em listas. (agencia (fixo "0001"), numero conta (sequencial, iniciando em 1) e usuário)
        Usuário pode ter mais de 1 conta, mas 1 conta só pode ter um usuário