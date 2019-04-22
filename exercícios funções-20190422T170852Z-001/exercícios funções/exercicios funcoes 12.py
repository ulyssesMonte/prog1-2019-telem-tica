

def f12(a) :
  i = 1
  while i * (i+1) * (i+2) < a:
     i = i + 1
  if i * (i+1) * (i+2) == a:
    return True
  else:
    return False