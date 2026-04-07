import os

os.system("Cls")
# Limpa o terminal.
# Cabeçalho.
# Função.
# Sem retorno.
def saudacao(nome):
  print(f"Ola, {nome}! Seja bem-vindo(a) ao nosso site.")

# Exemplo de uso da função.
nome_visitante = input("Digite seu nome: ")
saudacao(nome_visitante)
