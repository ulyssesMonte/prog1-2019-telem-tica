l=[0,0,0,0,0,0,0,0,0]
n=""
while n !="0":
  n=input("digite o nome do vendedor ")
  if n!="0":
    v=float(input("digite o valor de vendas brutas: "))
    s=200+(v*0.09)
    i=s//100
    if i > 1:
      if i>10:
        l[8]+=1
      else:
        l[i-2]+=1
for j in range(len(l)):
  if j!=8:
    c=(j+2)*100
    print(l[j]," vendedores ganham entre R$",c," e R$",c+99)
  else:
     print(l[j]," vendedores gaham R$ 1000 ou mais")