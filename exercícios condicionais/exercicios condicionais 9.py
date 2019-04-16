cod=int(input("Digite o códgo do consumidor"))
precokw=float(input("Digite o preço do Kw de energia: "))
quantkw=float(input("Digite a quantidade de Kw consumidos"))
total=precokw*quantkw
if total <11.20:
  print("O preço éé R$11.20")
else :
  print("O preço total é: R$", total)
