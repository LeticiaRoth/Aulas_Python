# Variáveis principais
nome_usuario = None
chave_acesso = None
sessao_ativa = False

def registrar_usuario():
    global nome_usuario, chave_acesso
    print("\n---------------------------")
    print("===== REGISTRO =====\n")
    if nome_usuario is None:
        nome_usuario = input("Escolha um nome de usuário: ")
        chave_acesso = input(f"Crie uma senha para {nome_usuario}: ")
        print(f"\nUsuário '{nome_usuario}' registrado com sucesso!")
    else:
        print(f"\nJá existe um usuário registrado: '{nome_usuario}'")

def acessar_sistema():
    global nome_usuario, chave_acesso, sessao_ativa
    if nome_usuario is not None:
        print("\n---------------------------")
        print("===== ENTRAR NO SISTEMA =====\n")
        nome_digitado = input("Digite seu nome de usuário: ")
        if nome_digitado.strip() == nome_usuario:
            senha_digitada = input(f"Digite a senha de {nome_usuario}: ")
            if senha_digitada.strip() == chave_acesso:
                sessao_ativa = True
                print("\nLogin efetuado com sucesso!")
            else:
                print("\nSenha incorreta.")
        else:
            print(f"\nUsuário '{nome_digitado}' não encontrado.")
    else:
        print("\nNenhum usuário foi registrado ainda.")

def redefinir_chave():
    global chave_acesso, sessao_ativa
    print("\n---------------------------")
    print("===== MUDAR SENHA =====\n")
    if sessao_ativa:
        tentativa = input("Confirme sua senha atual: ")
        if tentativa.strip() == chave_acesso:
            nova_senha = input("Digite a nova senha: ")
            chave_acesso = nova_senha
            print("\nSenha atualizada com sucesso!")
        else:
            print("\nSenha incorreta.")
    else:
        print("\nVocê precisa estar conectado para alterar a senha.")

def encerrar_sessao():
    global sessao_ativa
    print("\n---------------------------")
    print("===== LOGOUT =====\n")
    if sessao_ativa:
        confirmar = input("Deseja realmente sair? [SIM / NÃO]: ").strip().lower()
        if confirmar == "sim":
            sessao_ativa = False
            print("\nVocê saiu da sua conta.")
        elif confirmar == "não" or confirmar == "nao":
            print("\nLogout cancelado.")
        else:
            print("\nDigite apenas 'SIM' ou 'NÃO'.")
    else:
        print("\nVocê não está logado.")

def remover_conta():
    global nome_usuario, chave_acesso, sessao_ativa
    if sessao_ativa:
        print("\n---------------------------")
        print("===== EXCLUIR CONTA =====\n")
        confirmar = input("Tem certeza que deseja excluir a conta? [SIM / NÃO]: ").strip().lower()
        if confirmar == "sim":
            nome_usuario = None
            chave_acesso = None
            sessao_ativa = False
            print("\nConta excluída com sucesso.")
        elif confirmar == "não" or confirmar == "nao":
            print("\nA exclusão foi cancelada.")
        else:
            print("\nDigite apenas 'SIM' ou 'NÃO'.")
    else:
        print("\nÉ necessário estar logado para excluir a conta.")

def finalizar_programa():
    while True:
        escolha = input("\nTem certeza que deseja sair do sistema? [SIM / NÃO]: ").strip().lower()
        if escolha == "sim":
            print("\nEncerrando programa...")
            exit()
        elif escolha == "não" or escolha == "nao":
            print("\nCancelando encerramento...\n")
            break
        else:
            print("\nDigite apenas 'SIM' ou 'NÃO'.")

def painel_opcoes():
    while True:
        print("\n---------------------------")
        print("===== MENU PRINCIPAL =====\n")
        print("Escolha uma das opções:\n")
        print("1 - Registrar Novo Usuário")
        print("2 - Entrar no Sistema")
        print("3 - Mudar Senha")
        print("4 - Logout")
        print("5 - Excluir Conta")
        print("6 - Encerrar Programa\n")

        try:
            escolha = int(input("Digite o número da opção desejada: "))
            if escolha == 1:
                registrar_usuario()
            elif escolha == 2:
                acessar_sistema()
            elif escolha == 3:
                redefinir_chave()
            elif escolha == 4:
                encerrar_sessao()
            elif escolha == 5:
                remover_conta()
            elif escolha == 6:
                finalizar_programa()
            else:
                print("\nOpção inválida.")
        except ValueError:
            print("\nDigite apenas números.")


#Preciso retornar a função para funcionar
painel_opcoes()