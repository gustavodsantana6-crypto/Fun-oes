import os
os.system("cls")

def calcular_media(lista):
    """Retorna a média aritmética de uma lista de números."""
    return sum(lista) / len(lista) if lista else 0

def obter_estatisticas(lista):
    """Processa a lista e retorna um dicionário com os resultados."""
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    
    return {
        "qtd_pares": len(pares),
        "qtd_impares": len(impares),
        "qtd_positivos": len([n for n in lista if n > 0]),
        "qtd_negativos": len([n for n in lista if n < 0]),
        "qtd_total": len(lista),
        "maior": max(lista),
        "menor": min(lista),
        "media_pares": calcular_media(pares),
        "media_impares": calcular_media(impares),
        "media_total": calcular_media(lista),
        "inverso": lista[::-1]
    }

def executar_programa():
    """Função principal que coordena a entrada e saída."""
    numeros = []
    
    print("--- Sistema de Análise Numérica ---")
    for i in range(1, 6):
        while True:
            try:
                n = int(input(f"Digite o {i}º número inteiro: "))
                numeros.append(n)
                break
            except ValueError:
                print("Erro: Por favor, digite um número inteiro válido.")

    res = obter_estatisticas(numeros)

    print("\n" + "="*30)
    print(f"1. Pares: {res['qtd_pares']} | Ímpares: {res['qtd_impares']}")
    print(f"2. Positivos: {res['qtd_positivos']} | Negativos: {res['qtd_negativos']}")
    print(f"3. Total inserido: {res['qtd_total']}")
    print(f"4. Maior: {res['maior']} | Menor: {res['menor']}")
    print(f"5. Média Pares: {res['media_pares']:.2f}")
    print(f"6. Média Ímpares: {res['media_impares']:.2f}")
    print(f"7. Média Geral: {res['media_total']:.2f}")
    print(f"8. Ordem Inversa: {res['inverso']}")
    print("="*30)

if __name__ == "__main__":
    executar_programa()