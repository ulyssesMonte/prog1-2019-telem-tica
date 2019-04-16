fs=0
fn=0
ms=0
mn=0
for i in range(0,2000):
  resp=input("resposta ")
  sx=input("sexo ")
  if (resp.upper =="S")and(sx.upper=="F"):
    fs+=1
  elif (resp.upper =="N")and(sx.upper=="F"):
    fn+=1
  elif (resp.upper =="S")and(sx.upper=="M"):
    ms+=1
  elif (resp.upper =="N")and(sx.upper=="M"):
    mn+=1
print(fs+ms," pessoas responderam 'SIM' e ",fn+mn," pessoas responderam 'NÃO'")
pf=((fs+fn)*100)/2000
pm=((ms+mn)*100)/2000
print(pf,"% das pessoas que votaram são do sexo feminino e ",pm,"% são do sexo masculino")
pfs=(fs*100)/(fs+fn)
pmn=(mn*100)/(ms+mn)
print("A porcentagem de pessoas do sexo feminino que responderam sim: ",pfs,"%")
print("A porcentagem de pessoas do sexo masculino que responderam não: ",pmn,"%")
