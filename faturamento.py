import json

def carregar_faturamento_mensal(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        faturamento_mensal = json.load(arquivo)
    return faturamento_mensal

def calcular_estatisticas_faturamento(faturamento_mensal):
    valores_faturamento = [dia['valor'] for dia in faturamento_mensal['dias']]
    dias_com_faturamento = [dia['valor'] for dia in faturamento_mensal['dias'] if dia['valor'] > 0]
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    menor_valor = min(valores_faturamento)
    maior_valor = max(valores_faturamento)
    dias_acima_media = len([valor for valor in valores_faturamento if valor > media_mensal])
    return menor_valor, maior_valor, dias_acima_media

caminho_arquivo = 'faturamento_mensal.json'
faturamento_mensal = carregar_faturamento_mensal(caminho_arquivo)
menor_valor, maior_valor, dias_acima_media = calcular_estatisticas_faturamento(faturamento_mensal)

print("Estatísticas de Faturamento Mensal:")
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_media}")