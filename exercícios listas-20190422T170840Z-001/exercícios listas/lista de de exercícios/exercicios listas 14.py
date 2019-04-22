l=[]
t=0
l.append(input("Telefonou para a vítima?"))
l.append(input("Esteve no local do crime?"))
l.append(input("Mora perto da vítima?"))
l.append(input("Devia para a vítima?"))
l.append(input("Já trabalhou com a vítima?"))
l=l.upper()
for i in range (5):
  if l[i]=="S":
    t+=20
print(t,"% de chance de participação no crime")

