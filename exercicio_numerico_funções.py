import os

os.system("Cls")
# Limpa o terminal.
# Funções com parâmetro.
def tabuada(numero):
    for i in range(1,11):
      print(f"{numero} X {i} = {numero * (i)}")

# Exemplo de uso de função.
numero = int(input("Digite um numero para a tabuada: "))

# Chamando a função.
# Enviando parâmetros.
tabuada(numero)