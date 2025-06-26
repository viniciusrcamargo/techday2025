usuario_correto = "admin"
senha_correta = "12345"

usuario_digitado = input("Digite seu usuário: ")
senha_digitada = input("Digite sua senha: ")

if usuario_digitado == usuario_correto:
    if senha_digitada == senha_correta:
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")