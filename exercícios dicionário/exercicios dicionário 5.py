aux=0
d1={}
d2={}  
l=[]
j=0
x=True
while x==True:
  print("digite respectivamente nome, idade e cpf da pessoa a ser cadastrada")
  for i in range(3):
    l[i]=input(" ")
  l[1]=int(l[1])
  l[2]=int(l[2])
  d1[str(aux)]=l
  aux+=1
  y=input("Deseja cadastrar mais alguém? s/n ")
  if y.lower()=="s":
    pass
  else:
    x=False
for i in range(aux):
  if d1[str(i)][1]<18:
    d2[str(j)]=d1[str(i)]
    j+=1
    del(d1[str(i)])