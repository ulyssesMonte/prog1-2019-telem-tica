n1=float(input("Primeira nota: "))
n2=float(input("Segunda nota: "))
n3=float(input("Terceira nota: "))
media=0.0
media=(n1+n2+n3)/3
print("A média do aluo é: ",media)
if media<5.0:
  print("Conceito C")
elif (media>=5.0)and(media<8.0):
  print("Conceito: B")
elif (media >=8.0):
  print("Conceito A")
else:
  print("algo errado com os valores que foram digitados")
