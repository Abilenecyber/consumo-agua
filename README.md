 # 💧 Monitor de Consumo de Água - Conscientização Ambiental

> Solução computacional desenvolvida em Python fundamentada em um cenário hipotético de gestão de saneamento urbano, voltada à sensibilização e educação ambiental. O sistema atua na classificação de perfis de consumo imobiliário e na emissão de alertas educativos para moradores.

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

