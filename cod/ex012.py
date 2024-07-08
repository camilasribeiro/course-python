#Cálculo de um produto com 5% de desconto.
preco_prod = float(input('Qual é o preço do produto? R$ '))
desconto = preco_prod - (preco_prod * 0.05)
print(f'O valor com desconto é R$ {desconto:.2f}')
