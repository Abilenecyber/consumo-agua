# -*- coding: utf-8 -*-

print("=== SISTEMA DE CONSCIENTIZAÇÃO DE CONSUMO DE ÁGUA ===")

# Entrada de dados do usuário
tipo_imovel = input("Digite o tipo do imóvel (comercial, casa, apartamento): ").strip().lower()

# Definição das variáveis booleanas principais
eh_comercial = (tipo_imovel == "comercial")

# Início do fluxo de teste condicional
if eh_comercial:
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

else:
# Captura do consumo apenas para imóveis residenciais
    consumo = float(input("Digite o consumo de água em m³: "))
    
# Definição das variáveis booleanas residenciais
    eh_apartamento = (tipo_imovel == "apartamento")
    eh_casa = (tipo_imovel == "casa")
    consumo_economico = (consumo < 10.0)
    consumo_moderado = (consumo <= 25.0)

# Validação das regras residenciais
    if eh_apartamento and consumo_economico:
        print("Consumo econômico – excelente controle de água!")

    elif (eh_apartamento or eh_casa) and consumo_moderado and not eh_comercial:
        print("Consumo moderado – dentro do padrão residencial.")
       
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
