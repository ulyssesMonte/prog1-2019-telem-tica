l=[]
PAR=[]
IMPAR=[]
for i in range (20):
  print(i)
  l.append(int(input("digite um n�mero")))
  if (l[i] % 2 ==0):
    PAR.appened(l[i])
  else:
    IMPAR.appened(l[i])
print(l,"\n",PAR,"\n",IMPAR)

