a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))

area = a * l
print('Área da parede: {}m²'.format(area))
litros = area / 2
print('Quantidade de tinta: {:.2f}L'.format(litros))

