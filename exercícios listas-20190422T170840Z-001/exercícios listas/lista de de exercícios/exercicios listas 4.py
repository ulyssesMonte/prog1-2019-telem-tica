l=[]
ls=""
c=0
for i in range (10):
  ls=(input("digite uma letra")).upper()
  if (ls=="A") or (ls=="E") or (ls=="I") or (ls=="O") or (ls=="U"):
    pass
  else:
    l.append(ls)
    c+=1
print(l,"\n",c)

