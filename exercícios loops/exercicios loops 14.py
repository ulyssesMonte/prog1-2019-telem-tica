total=0
n5=0
n7=0
n10=0
n12=0
c=True
while c===True:
  ent=int(input("Digite, o numero do canal que estáá assistindo: ou digite 0 para encerrar a pesquisa"))
  if ent!=0;
    total+=1
    if ent==5:
      n5+=1
    elif ent==7:
      n7+=1
    elif ent==10:
      n10+=1
    elif ent==12:
      n12+=1
    else:
      print("valor inválido")
  else:
    c=False

n5=(n5*100)/total
n7=(n7*100)/total
n10=(n10*100)/total
n12=(n12*100)/total
print("o canal 5 representa ",n5,"% da audiência")
print("o canal 7 representa ",n7,"% da audiência")
print("o canal 10 representa ",n10,"% da audiência")
print("o canal 12 representa ",n12,"% da audiência")
