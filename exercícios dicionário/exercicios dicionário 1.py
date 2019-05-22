vogaisConsideradas={ "A":0,"E":0,"I":0,"O":0,"U":0}
x=True
while x==True:
  e=input("Digite uma letra ")
  if e.upper()=="A":
    vogaisConsideradas["A"]+=1
  elif e.upper()=="E":
    vogaisConsideradas["E"]+=1
  elif e.upper()=="I":
    vogaisConsideradas["I"]+=1
  elif e.upper()=="O":
    vogaisConsideradas["O"]+=1
  elif e.upper()=="U":
    vogaisConsideradas["U"]+=1
  else:
    x=False
print(vogaisConsideradas)