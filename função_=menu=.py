import os
os.system("cls")
# Limpa o terminal.
# Função sem parâmetros e com retorno.

print(r"""
▓█████▄  ▄▄▄       ███▄    █  ▄████▄   ▒█████  
▒██▀ ██▌▒████▄     ██ ▀█   █ ▒██▀ ▀█  ▒██▒  ██▒
░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄ ▒██░  ██▒
░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██   ██░
░▒████▓  ▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░░ ████▓▒░
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒░▒░▒░ 
 ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒     ░ ▒ ▒░ 
 ░ ░  ░   ░   ▒      ░   ░ ░ ░        ░ ░ ░ ▒  
   ░          ░  ░         ░ ░ ░          ░ ░     /
 ░                           ░                

        >>> BANCO ORBIX <<<
        Sistema Financeiro Avançado     
""")

def menu():
    print("1 - Criar")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Saldo")
    print("5 - Sair")
    return

def criar_usuario():
    print("Criando usuário...")
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    print(f"Usuário {usuario} criado com sucesso!")
    return

def sacar_dinheiro():
    print("Sacando dinheiro...")
    valor = float(input("Digite o valor a ser sacado: "))
    print(f"Valor de R${valor} sacado com sucesso!")
    return


def depositar_dinheiro():
    print("Depositando dinheiro...")
    valor = float(input("Digite o valor a ser depositado: "))
    print(f"Valor de R${valor} depositado com sucesso!")
    return

def verificar_saldo():
    print("Verificando saldo...")
    saldo = 10000.00
    print(f"Seu saldo atual é: R${saldo}")
    return

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        criar_usuario()
    elif escolha == "2":
        sacar_dinheiro()
    elif escolha == "3":
        depositar_dinheiro()
    elif escolha == "4":
        verificar_saldo()
    elif escolha == "5":
        print("Obrigado pela preferência! Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")                