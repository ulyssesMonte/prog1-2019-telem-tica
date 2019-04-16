preco=0.0
total=0
while cod != "x":
  cod=input("Digite o código do item que você deseja comprar: ")
  cod=cod.upper
  quant=float(input("Digite a quantidade que você deseja comprar desse item: "))
  if cod=="H":
    preco+=1.50
  elif cod=="C":
    preco+=1.80
  elif cod=="M":
    preco+=1.20
  elif cod=="A":
    preco+=2.00
  elif cod=="Q":
    preco+=1.00
  total+=preco*quant
print("Total a pagar: R$", total)
