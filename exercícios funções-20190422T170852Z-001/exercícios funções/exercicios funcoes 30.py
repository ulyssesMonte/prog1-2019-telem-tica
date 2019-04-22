def f30(m1,m2):
  r=True
  for i in len(m1):
    for j in len(m1[0]):
      if m1[i],[j] != m2[i],[j]:
        r=False
        break
  return r
