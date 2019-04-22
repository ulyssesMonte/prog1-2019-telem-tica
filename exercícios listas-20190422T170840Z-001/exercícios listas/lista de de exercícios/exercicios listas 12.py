I=[]
a=[]
m=0.0
r=0
for i in range (30):
  I.append(int(input("digite sua idade")))
  a.append(float(input("digite sua altura")))
  m+=a[i]
m=m/30
for i in range (30):
  if (idade[i]>13) and (altura[i]<m):
    r+=1
print(r)

