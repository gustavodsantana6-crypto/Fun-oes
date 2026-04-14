import os
os.system("cls")

# Limpa o terminal.
# Função com parâmetros e retornos.
def calcular_imc(peso, altura):
    """Calcula o IMC e retorna o valor."""
    return peso / (altura ** 2)

def obter_classificacao(imc):
    """Recebe o IMC e retorna uma tupla com (classificação, recomendação)."""
    if imc < 18.5:
        return "Abaixo do peso", "Consulte um nutricionista para orientação"
    elif 18.5 <= imc < 25:
        return "Peso normal", "Mantenha hábitos saudáveis!"
    elif 25 <= imc < 30:
        return "Sobrepeso", "Considere uma dieta balanceada e atividade física"
    elif 30 <= imc < 35:
        return "Obesidade grau 1", "Procure orientação de um profissional de saúde"
    elif 35 <= imc < 40:
        return "Obesidade grau 2", "Consulte um médico para avaliação e orientação"
    else:
        return "Obesidade grau 3", "Busque assistência médica imediatamente"

def main():
    """Função principal que executa o fluxo do programa."""
    print("--- Calculadora de IMC ---")
    
    try:
        # Entrada de dados
        p = float(input("Digite seu peso em kg: "))
        a = float(input("Digite sua altura em metros: "))

        # Processamento
        valor_imc = calcular_imc(p, a)
        classe, dica = obter_classificacao(valor_imc)

        # Saída de dados
        print("-" * 30)
        print(f"Seu IMC: {valor_imc:.2f}")
        print(f"Classificação: {classe}")
        print(f"Recomendação: {dica}")
        print("-" * 30)
        
    except ValueError:
        print("Erro: Por favor, insira apenas números usando ponto para decimais.")

# Inicia o programa
if __name__ == "__main__":
    main()
