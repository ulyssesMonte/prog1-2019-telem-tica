print("digite M para matutino, V para vespertino e N para noturno")
turno=input("Em qual turno você estuda?")
turno=turno.upper
if turno=="M":
  print("Bom dia")
elif turno=="V":
  print("Boa tarde")
elif turno=="N":
  print("Boa noite")
else:
  print("Você digitou um valor inválido")
