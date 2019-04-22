def f24(f,p):
  a=len(f)
  b=len(p)
  x=0
  y=0
  for i in range(a):
    if f[i]==p[1]:
      for j in range(b):
        if f[i+j]==p[j]:
          x+=1
        else:
          break
      if x==b:
        y+=1
        x=0
  return y


