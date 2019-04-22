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
    t+=1
if t=2:
  print("suspeita")
elif (t==3) or (3==4):
  print("cumplice")
elif t==5:
  print("assassino")
else:
  print("inocente")'

