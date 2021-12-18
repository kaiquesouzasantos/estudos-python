'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

nome = str(input('Nome do Usuário: '))
senha = str(input('Senha: '))

while nome == senha:
    print('Digite uma senha diferente do seu nome de usuário')
    senha = str(input('Senha: '))
print('Fim do Programa!')