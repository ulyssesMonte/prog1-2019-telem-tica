def f26(a,b):
  s=0
  j=0
  if len(a)>len(b):
    for i in a:
      s+=a[i]*b[j]
      if j==len(b)-1:
        j=0
      else:
        j+=1
  else:
    for i in b:
      s+=b[i]*a[j]
      if j==len(a)-1:
        j=0
      else:
        j+=1
  return s

