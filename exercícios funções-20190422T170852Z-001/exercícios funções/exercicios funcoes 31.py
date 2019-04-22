def maior(l1):
  a=len(l1)
  m=-1000
  for i in range(a):
    if l1[i]>m:
      m=l1[i]
  return m

def soma(l1):
  a=len(l1)
  s=0
  for i in range (a):
    s+=l1[i]
  return s 

def ocorrencia(l1):
  a=len(l1)
  o=0
  for i in range(a):
    if l1[1]==l1[i]:
      o+=1
  return o

def media(l1):
  a=len(l1)
  s=soma(l1)]
  m=s/a
  return m

def valor(l1):
  m=media(l1)
  l2=[]
  for i in l1:
    l2.append(l1[i]-media)
    if l2[i]<0:
      l2[i]=l2[i]*-1
  v=maior(l2)
  return v

def somaValor(l1):
  s=soma(l1)
  v=valor(l1)
  sv=s+v 
  return sv