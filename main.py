# TRABALHO PRÁTICO - ALGORITMOS E PROGRAMAÇÃO
# Sistema de Atendimento e Pedidos em Python
# Estudante: Glauco Antonio Braz Ferreira

# Função para apresentar o cardápio
def mostrar_cardapio():
    print("\n========== CARDÁPIO ==========")
    print("1 - X-Burger        - R$ 18.00")
    print("2 - X-Salada        - R$ 20.00")
    print("3 - X-Bacon         - R$ 23.00")
    print("4 - Batata Frita    - R$ 12.00")
    print("5 - Refrigerante    - R$ 7.00")
    print("0 - Finalizar pedido")
    print("===============================")

# Função para identificar o produto e o respetivo preço
def escolher_produto(codigo):
    if codigo == 1:
        nome = "X-Burguer"
        preco = 18.00
    elif codigo == 2:
        nome = "X-Salada"
        preco = 20.00
    elif codigo == 3:
        nome = "X-Bacon"
        preco = 23.00
    elif codigo == 4:
        nome = "Batata Frita"
        preco = 12.00
    elif codigo == 5:
        nome = "Refrigerante"
        preco = 7.00
    else:
        nome = ""
        preco = 0.0

    return nome, preco

# Função para calcular o desconto com base nas regras estabelecidas
def calcular_desconto(total):
    if total < 50.0:
        percentual = 0
    elif total < 100.0:
        percentual = 5
    else:
        percentual = 10

    valor_desconto = total * percentual / 100.0
    valor_final = total - valor_desconto

    return percentual, valor_desconto, valor_final

# Função para escolher a forma de pagamento com validação
def escolher_pagamento():
    while True:
        print("\n========== PAGAMENTO ==========")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")

        opcao = int(input("Escolha a forma de pagamento (1, 2 ou 3): "))

        if opcao == 1:
            return "Dinheiro"
        elif opcao == 2:
            return "PIX"
        elif opcao == 3:
            return "Cartão"
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

# INÍCIO DO PROGRAMA PRINCIPAL
def main():
    print("======================================")
    print("      SISTEMA DE ATENDIMENTO")
    print("======================================")

    nome_cliente = input("Digite o nome do cliente: ")
    total = 0.0

    # Estrutura de repetição para os pedidos (while)
    while True:
        mostrar_cardapio()

        codigo = int(input("Digite o código do produto: "))

        # Verifica se o cliente deseja finalizar o atendimento
        if codigo == 0:
            break

        # Identifica o produto e o preço escolhido
        nome_produto, preco = escolher_produto(codigo)

        # Validação do código do produto
        if preco == 0.0:
            print("Código inválido! Escolha um produto do cardápio.")
        else:
            quantidade = int(input("Digite a quantidade desejada: "))

            # Validação da quantidade
            if quantidade <= 0:
                print("Quantidade inválida! Deve ser maior que zero.")
            else:
                subtotal = preco * quantidade
                total = total + subtotal

                print("\nProduto:", nome_produto)
                print("Quantidade:", quantidade)
                print("Subtotal: R$", format(subtotal, ".2f"))
                print("Total acumulado: R$", format(total, ".2f"))

    # Validação caso nenhum produto seja adicionado
    if total == 0.0:
        print("\nNenhum produto foi selecionado. O atendimento foi encerrado.")
    else:
        # Cálculo do desconto
        percentual, valor_desconto, valor_final = calcular_desconto(total)

        # Seleção da forma de pagamento
        pagamento = escolher_pagamento()

        # Resumo final da compra
        print("\n======================================")
        print("         RESUMO DA COMPRA")
        print("======================================")
        print("Cliente:", nome_cliente)
        print("Valor original: R$", format(total, ".2f"))
        print("Desconto aplicado:", str(percentual) + "%")
        print("Valor do desconto: R$", format(valor_desconto, ".2f"))
        print("Valor final: R$", format(valor_final, ".2f"))
        print("Forma de pagamento:", pagamento)
        print("======================================")
        print("Obrigado pela preferência!")

# Execução do programa
if __name__ == "__main__":
    main()