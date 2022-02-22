# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

user = input('Informe um nome de usuário: ')
pass_ = input('Informe uma senha: ')

while user == pass_:
    print('Usuário e senha não podem ser iguais, por favor digite novamente')
    user = input('Informe um nome de usuário: ')
    pass_ = input('Informe uma senha: ')
