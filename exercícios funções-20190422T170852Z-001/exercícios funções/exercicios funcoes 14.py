
def f14(x,y) :
  s=0
  if x>y:
    for i in range(x,y):
      if i%2!=0:
        s+=i
  else:
    for i in range(y,x,-1):
      if i%2!=0:
        s+=i
  return s