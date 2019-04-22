def maiorElemento(s1):
  a=len(s1)
  c=0
  e=[]
  k=0
  me=[]
  for i in range(a):
    if s1[i]==" ":
      for j in range(c,i+1):
        e[k]=s1[j]
        k+=1
      k=0
      c=i
      if len(e)>len(me):
        me=e
  return me

def mediaVogais(s1):
  a=len(s1)
  c=0
  e=[]
  k=0
  qv=[]
  s=0
  for i in range(a):
    if s1[i]==" ":
      for j in range(c,i+1):
        e[k]=s1[j]
        k+=1
      k=0
      c=i
      for l in e:
        if (e[l].upper=="A") or (e[l].upper=="E") or (e[l].upper=="I") or (e[l].upper=="O") or (e[l].upper=="U"):
          q+=1
      qv.appen(q)
  for m in qv:
    s+=qm[m]
  mv=s/len(qv)
  return mv

def ocorrencia(s1):
  a=len(s1)
  o=0
  for i in range(a):
    if s1[1]==s1[i]:
      o+=1
  return o