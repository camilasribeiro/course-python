#Convertendo metros para centímetros e milímetros.
medida = float(input('Insira a quantidade de metros: '))
cm = medida * 100
mm = medida * 1000
print(f'{medida}m tem {cm:.0f}cm')
print(f'{medida}m tem {mm:.0f}mm')
