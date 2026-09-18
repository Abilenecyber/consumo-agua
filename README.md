 # 💧 Monitor de Consumo de Água - Conscientização Ambiental

> Solução computacional desenvolvida em Python fundamentada em um cenário hipotético de gestão de saneamento urbano, voltada à sensibilização e educação ambiental. O sistema atua na classificação de perfis de consumo imobiliário e na emissão de alertas educativos para moradores.

---
##  🎯  Objetivo
Implementar a classificação de acordo com as seguintes regras de negócio: 
> Se o tipo for "comercial", exibir: "Tarifa comercial aplicada – consulte o plano corporativo."
>Se o tipo for "apartamento" e o consumo for menor que 10 m<sup>3</sup>, exibir: "Consumo econômico – excelente controle de água!"
>Se o tipo for "apartamento" ou for "casa" com consumo de até 25 m<sup>3</sup>, exibir: "Consumo moderado – dentro do padrão residencial."
>Em qualquer outro caso (consumo acima do limite residencial), exibir: "Consumo excessivo – adote medidas de economia e verifique vazamentos.

---

## 🛠️ Linguagem Usada


<div style="display: inline_block"><br> 
<img align="center" alt="Python" height="40" width="40" 
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"> 
</div>

---

## 🎯 Foco Didático: Operadores Lógicos

Para atender às regras de negócio propostas pela companhia de saneamento, o script utiliza de forma clara os três operadores lógicos essenciais:

*   **`and` (E):** Utilizado para validar se o imóvel é um apartamento **E** se o consumo está na faixa econômica (menor que 10 m³).
*   **`or` (OU):** Aplicado para permitir caminhos alternativos de validação residencial, aceitando que o imóvel seja uma casa **OU** um apartamento.
*   **`not` (NÃO):** Inserido como um filtro extra de segurança, garantindo de forma limpa que a regra residencial **NÃO** seja executada caso o imóvel seja comercial.

---

## 🚀 Como Executar o Programa

### Pré-requisitos
Você precisa ter o **Python 3.x** instalado no computador.

### Passo a Passo no Terminal

1. **Navegue até a subpasta do projeto:**
   ```bash
   cd consumo-agua
   ```

2. **Execute o script:**
   ```bash
   python app.py
   ```

