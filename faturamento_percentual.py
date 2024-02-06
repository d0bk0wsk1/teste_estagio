def calcular_percentual_faturamento(faturamento_estados):
    total_faturamento = sum(faturamento_estados.values())
    percentuais = {estado: (faturamento / total_faturamento) * 100 for estado, faturamento in faturamento_estados.items()}
    return percentuais

faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

percentuais = calcular_percentual_faturamento(faturamento_estados)
print("Percentual de representação de cada estado no faturamento mensal:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f} %")

