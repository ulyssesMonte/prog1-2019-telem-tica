def contagem(x):
  if x!=-1:
    print(x)
    y=x-1
    contagem(y)
a=int(input("digite o tempo para ser contado regressivamente "))
contagem(a)
print("boom!")