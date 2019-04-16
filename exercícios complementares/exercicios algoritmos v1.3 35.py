nome=input("nome ")
n1=float(input("digite sua nota em portugês"))
n2=float(input("digite sua nota em matemática"))
n3=float(input("digite sua nota em conhecimentos gerais"))
media=(n1+n2+n3)/3
if (media>7.0) and (n1>5.0) and (n2>5.0) and (n3>5.0):
  print("APROVADO!")
else:
  print("reprovado :/")

