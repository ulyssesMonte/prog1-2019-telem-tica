l1=[]
l2=[]
l3=[]
l4=[]
for i in range (10):
  l1.append(int(input("digite um número para o vetor 1: ")))
for i in range (10):
  l2.append(int(input("digite um número para o vetor 2: ")))
for i in range (10):
  l3.append(int(input("digite um número para o vetor 3: ")))
for i in range (10):
  l4.append(l1[i])
  l4.append(l2[i])
  l4.append(l3[i])
print(l4)

