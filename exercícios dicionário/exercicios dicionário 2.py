l=[]
d={"aluno":" ","n1":0,"n2":0}
x=True
while x==True:
  d["aluno"]=input("nome ")
  if d["aluno"]!="":
    d["n1"]=float(input("nota 1 "))
    d["n2"]=float(input("nota 2 "))
    l.append(d)
  else:
    x=False
m=input("digite o nome do aluno que deseja ver a média ")
for i in range(len(l))
  if l[i]["aluno"]==m:
    print("A média de ",m," é ",((l[i]["n1"]+l[i]["n2"])/2))