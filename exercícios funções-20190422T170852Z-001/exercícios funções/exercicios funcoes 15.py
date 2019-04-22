

def f15(a):
  q = a
  b = 0
  Pot = 1
  while q>0 :
    d = q // 2
    r = q % 2
    q = d
    b = b+(r*Pot)
    Pot = Pot*10
  return b
