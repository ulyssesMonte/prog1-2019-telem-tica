l1=[]
l2=[]
l3=[]
for i in range (10):
  l1.append(int(input("digite um número para o vetor 1: ")))
for i in range (10):
  l2.append(int(input("digite um número para o vetor 2: ")))
for i in range (10):
  l3.append(l1[i])
  l3.append(l2[i])
print(l3)

