# Definindo uma lista vazia para armazenar os usuários cadastrados
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    print("Digite as informações do novo usuário:")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    cidade = input("Cidade: ")
    idade = int(input("Idade: "))
    
    # Verificando se o usuário já existe na lista
    for usuario in usuarios:
        if usuario['email'] == email:
            print("Usuário já cadastrado!")
            return
    
    # Adicionando o novo usuário à lista
    usuarios.append({
        'nome': nome,
        'email': email,
        'senha': senha,
        'cidade': cidade,
        'idade': idade
    })
    
    print("Usuário cadastrado com sucesso!")
    

# Função para fazer login
def fazer_login():
    print("Digite suas informações de login:")
    email = input("E-mail: ")
    senha = input("Senha: ")
    
    # Verificando se o usuário existe na lista
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print(f"Bem-vindo, {usuario['nome']}!")
            return
    
    print("E-mail ou senha incorretos!")
    

# Menu principal
while True:
    print("Escolha uma opção:")
    print("1 - Cadastrar novo usuário")
    print("2 - Fazer login")
    print("3 - Sair")
    
    opcao = input()
    
    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        fazer_login()
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida!")