peso=float(input("Digite o seu peso: "))
altura=float(input("Digite a sua altura"))
imc= peso/(altura*altura)

if imc<26:
  print("você está normal")
elif (imc>=26) and (imc<30):
  print("você estáá obeso")
else:
  print("você está obeso mórbido")
