from controller import ControllerCadastro, ControllerLogin

while True:
    print("==========[Menu]==========")
    decidir = int(input('Digite 1 para cadastro\nDigite 2 para Logar\nDigite 3 para sair\n'))

    if decidir == 1:
        nome = input('Digite o seu nome: ')
        email = input('Digite o seu email: ')
        senha = input('Digite a sua senha: ')
        resultado = ControllerCadastro.cadastrar(nome, email,senha)

        if resultado == 2:
            print("Tamanho do nome digitado é inválido")
        elif resultado == 3:
            print("email maior que 200 caracteres")
        elif resultado == 4:
            print("Tamanho de senha inválido")
        elif resultado == 5:
            print("Email já cadastrado")
        elif resultado == 6:
            print("Erro interno do sistema")
        elif resultado == 1:
            print("Cadastro realizado com sucesso")
    elif decidir == 2:
        email = input('Digite o seu email: ')
        senha = input('Digite a sua senha: ')
        resultado = ControllerLogin.login(email, senha)
        if not resultado:
            print("Email ou senha inválidos")
        else:
            print(resultado)
    else:
        break
        
   