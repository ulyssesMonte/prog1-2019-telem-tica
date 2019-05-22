d1={}
d2={}
aux=0
x=True
while x==True:
  for i in range(5):
    d1[str(i)]=input("digite dados ")
  for i in range(5):
    d2[str(aux)+"-"+str(i)]=d1[str(i)]
    del(d1[str(i)])
  aux+=1
  y=input("Deseja continuar? s/n ")
  if y.lower()=="s":
    pass
  else:
    x=False
print("BACKUP: ",d2)