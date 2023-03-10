import json

def faturamento():
    with open('dados_faturamento.json') as arquivo:
        dados = json.load(arquivo)

    faturamento_diario = dados['faturamento_diario']

    soma = 0
    qtd_dias = 0
    for faturamento in faturamento_diario:
        if faturamento != 0:
            soma += faturamento
            qtd_dias += 1
    media = soma / qtd_dias

    menor = min(faturamento_diario)
    maior = max(faturamento_diario)

    acima_media = 0
    for faturamento in faturamento_diario:
        if faturamento > media:
            aci_media += 1

    print(f"Menor faturamento diário: R$ {menor:.2f}")
    print(f"Maior faturamento diário: R$ {maior:.2f}")
    print(f"Dias acima da média: {acima_media}")

if __name__ == '__main__':
    faturamento()