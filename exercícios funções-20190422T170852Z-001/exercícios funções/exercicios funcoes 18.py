
def f18(a,b):
  c=len(b)
  d=0
  for i in range(c):
    if a==b[i]:
      d+=i
  return d
