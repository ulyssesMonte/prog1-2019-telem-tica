l=[]
media=[0,0,0]
d={"nome":"","v1":0.0,"v2":0.0,"v3":0.0,"v4":0.0,"v5":0.0}
for i in range(3):
  d["nome"]=input("nome ")
  for i in range(1,6):
    v="v"+str(i)
    d[v]=float(input("tempo da ",i,"° volta "))
  l.append(d)
menor=d["v1"]
for i in range(3):
  for j in range(1,6):
    v="v"+str(i)
    media[i]+=l[i][v]
    if l[i][v]<menor:
      menor=l[i][v]
      m1=l[i]["nome"]
      mv=j
  media[i]=media[i]/5
melhor=media[i]
pior=media[i]
for i in range(3):
  if media[i]<=melhor:
    melhor=media[i]
    m2=l[i]["nome"]
  if  media[i]>=pior:
    pior=media[i]
    p=l[i]["nome"]
for i in range(3):
  if (l[i]["nome"]!=melhor)and(l[i]["nome"]!=pior)
  m3=l[i]["nome"]
print("Em primeiro lugar temos: ",m2," em segundo ",m3,"e em terceiro ",p)
print("a melhor volta foi a ",mv," de ",m1," sendo de ",menor," segundos" )