t=["janeiro",0,"fevereiro",0,"março",0,"abril",0,"maio",0,"junho",0,"julho",0,"agosto",0,"setembro",0,"outubro",0,"novembro",0,"dezembro",0]
m=0
for i in range (1,24,2):
  t[i]=(int(input("digite a temperatura média do mês: ")))
  m+=t[i]
m=m/12
for i in range (1,24,2):
  if t[i]>m:
    print(t[i],"-",t[i-1])

