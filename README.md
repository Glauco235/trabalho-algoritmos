# Sistema de Atendimento e Pedidos em Python

* **Estudante:** Glauco Antonio Braz Ferreira
* **Disciplina:** Algoritmos e Programação
* **Instituição:** Unilavras

## Descrição do Projeto
Este projeto consiste num sistema desenvolvido em linguagem Python para automatizar o atendimento e o registo de pedidos de uma lanchonete. O programa substitui o registo manual por uma solução digital interativa, permitindo escolher produtos do cardápio, calcular subtotais, aplicar regras progressivas de desconto e gerir formas de pagamento.

## Principais Funcionalidades Implementadas
* **Identificação do Cliente:** Registo inicial do nome do cliente.
* **Cardápio Interativo:** Apresentação de 5 produtos com respetivos códigos e preços fixos.
* **Acumulação de Valores:** Cálculo dinâmico do subtotal e acumulação no total da compra sem necessidade de estruturas de dados complexas.
* **Controlo de Repetição:** Execução contínua através da estrutura `while` até que o utilizador decida finalizar com o código `0`.
* **Validação de Dados:** Tratamento de códigos de produtos inexistentes e quantidades inválidas (negativas ou nulas).
* **Regras de Desconto Progressivo:**
  * Abaixo de R$ 50,00: Sem desconto (0%).
  * De R$ 50,00 até R$ 99,99: 5% de desconto.
  * Igual ou superior a R$ 100,00: 10% de desconto.
* **Gestão de Pagamento:** Seleção validada entre Dinheiro, PIX ou Cartão.
* **Resumo Final:** Emissão detalhada com o valor original, desconto, valor final e forma de pagamento.

## Instruções para Executar o Programa
1. Certifique-se de que tem o **Python 3** instalado no seu computador.
2. Faça o clone ou descarregue os ficheiros deste repositório.
3. Abra o terminal (ou prompt de comando) na pasta onde se encontra o ficheiro `main.py`.
4. Execute o seguinte comando:
   ```bash
   python3 main.py