l=[]
t=0
l.append(input("Telefonou para a v�tima?"))
l.append(input("Esteve no local do crime?"))
l.append(input("Mora perto da v�tima?"))
l.append(input("Devia para a v�tima?"))
l.append(input("J� trabalhou com a v�tima?"))
l=l.upper()
for i in range (5):
  if l[i]=="S":
    t+=20
print(t,"% de chance de participa��o no crime")

