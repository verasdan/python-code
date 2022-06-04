preco = float(input('Digite o preço do produto: '))
desconto = preco * 5/100
precoComDesconto = preco - desconto
print(f'(O desconto de 5% deste Produto = {desconto} reais\nNovo preço do Produto = {precoComDesconto} reais')
input()