# Identificação
print('Bem-vindo a Loja de Adriana C. G. Thume RU 1902469')

# Try para evitar erro quando o usuário digitar um valor não numérico
try:
    # Entrada dos dados pelo usuário
    valor = float(input('Entre com o valor do produto: '))
    quantidade = int(input('Entre com a quantidade: '))

    # Cálculos dos valores
    valorSemDesconto = valor * quantidade

    valorDesconto = 0

    if quantidade <= 9:
        valorDesconto = 0
    elif quantidade <= 99:
        valorDesconto = valorSemDesconto * 0.05
    elif quantidade <= 999:
        valorDesconto = valorSemDesconto * 0.10
    else:
        valorDesconto = valorSemDesconto * 0.15

    valorComDesconto = valorSemDesconto - valorDesconto

    # Saída dos dados
    print('O valor sem desconto foi: R$ {:.2f}'.format(valorSemDesconto))
    print('O valor com desconto foi: R$ {:.2f}'.format(valorComDesconto))

# Mensagem do erro
except ValueError:
    print('Foi inserido um valor não numérico')
