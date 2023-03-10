def faturamento_mensal():
    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    total = sum(faturamento.values())
    porcentagens = {}
    for estado, valor in faturamento.items():
        porcentagem = (valor / total) * 100
        porcentagens[estado] = porcentagem

    for estado, percentual in porcentagens.items():
        print(f"{estado}: {percentual:.2f}%")
    return


if __name__ == '__main__':
    faturamento_mensal()