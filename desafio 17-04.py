l=[50,2,100,3] #variável global
def entrada():
  i=0
  e=-1
  while e !=0:
    e=int(input("digite um valor"))
    l.append(e)
    i+=1

def maior():
  a=len(l)
  m=-10000
  for i in range(a):
    if l[i]> m:
      m=l[i]
  return m

def menor():
  a=len(l)
  m=10000
  for i in range(a):
    if l[i]< m:
      m=l[i]
  return m

def ordenarC():
  lo=l
  t=0
  a=len(lo)
  for i in range(a):
    for j in range(a):
      if i!=j:
        if lo[i] < lo[j]:
          t=lo[i]
          lo[i]=lo[j]
          lo[j]=t
  return lo
        
def ordenarD():
  ld=l
  t=0
  a=len(ld)
  for i in range(a):
    for j in range(a):
      if i!=j:
        if ld[i] > ld[j]:
          t=ld[i]
          ld[i]=ld[j]
          ld[j]=t
  return ld
  

while True:
  print("digite 0 para escrever numeros em uma lista")
  print("digite 1 para ler a lista")
  print("digite 2 para ver o maior numero da lista")
  print("digite 3 para ver o menor numero da lista")
  print("digite 4 para ver a lista em ordem crescente")
  print("digite 5 para ver a lista em ordem decrescente")
  print("digite 6 para sair")
  e=input()
  if e==0:
    entrada()
  elif e=="1":
    print(l)
  elif e=="2":
    print(maior())
  elif e=="3":
    print(menor())
  elif e=="4":
    print(ordenarC())
  elif e=="5" :
    print(ordenarD())
  elif e=="6":
    break
  else:
    print("digite um valor válido ")