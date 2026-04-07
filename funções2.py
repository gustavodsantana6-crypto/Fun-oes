import os

os.system("Cls")
# Limpa o terminal.
# Funções com parâmetros.
# Com retorno.
def somar(n1,n2):
    soma = (n1 + n2)
    return soma

# Exemplo de uso de funções.
n1 = int(input("Digite seu primeiro numero: "))
n2 = int(input("Digite seu segundo numero: ")) 

# Chamando a função.
# Enviando parâmetros.
resultado = somar(n1,n2)

print(f"Soma: {resultado}")