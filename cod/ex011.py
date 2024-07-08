#Calculando a quantidade de tinta usada para pintar uma parede de acordo com sua área.
largura = int(input('Qual é a largura da parede? '))
altura = int(input('Qual é a altura da parede? '))
area = largura * altura
qtd_tinta = area / 2
print(f'Será necessário {qtd_tinta} litros de tinta para pintar a parede.')
