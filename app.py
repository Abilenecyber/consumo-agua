# -*- coding: utf-8 -*-

print("=== SISTEMA DE CONSCIENTIZAÇÃO DE CONSUMO DE ÁGUA ===")

# 1. Pegando os dados do morador
tipo_imovel = input("Digite o tipo do imóvel (comercial, casa, apartamento): ").strip().lower()
consumo = float(input("Digite o consumo de água em m³: "))

# 2. Criando variáveis de teste de forma simples (Igual aos exemplos da aula)
eh_comercial = (tipo_imovel == "comercial")
eh_apartamento = (tipo_imovel == "apartamento")
eh_casa = (tipo_imovel == "casa")

# Faixas de consumo separadas
consumo_economico = (consumo < 10.0)
consumo_moderado = (consumo <= 25.0)

# --- REGRAS ---

# REGRA 1: Se for comercial
if eh_comercial:
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

# REGRA 2: Se for apartamento E o consumo for econômico (Exemplo do operador AND)
elif eh_apartamento and consumo_economico:
    print("Consumo econômico – excelente controle de água!")

# REGRA 3: Se for apartamento OU casa com consumo padrão (Exemplo do operador OR + NOT)
# Usamos o NOT para garantir com clareza total que NÃO é um imóvel comercial.
elif (eh_apartamento or eh_casa) and consumo_moderado and not eh_comercial:
    print("Consumo moderado – dentro do padrão residencial.")

# REGRA 4: Qualquer outro caso
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")