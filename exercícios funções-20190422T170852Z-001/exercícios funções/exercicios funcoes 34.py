q=int(input("digite a quantidade de alunos "))
m=[]
def constroi():
  for i in range(q):
    list.append(m,[0]*2)

def ler():
  for i in range(q):
    for j in range (2):
      if j==0:
        m[i],[j]=int(input("Digite sua idade"))
      else:
        m[i],[j]=float(input("Digite sua altura"))

def MediaTurma(l):
  soma=0
  for i in range(q):
    soma+=l[q][1]
  media=soma/q
  return media

def Conta_Baixinhos(l,media):
  baixinhos=0
  for i in range(q):
    if (l[i][1]>13)and(l[i][2]<media):
      baixinhos+=1
  return baixinhos
