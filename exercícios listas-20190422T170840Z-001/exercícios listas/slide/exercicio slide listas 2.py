l1=[1,2,3,4,5]
l2=[5,4,3,2,1]
l3=[]
l4=[]
tam=5
for i  in range(tam) :
  l3.append(l1[i]+l2[i])
for j  in range(tam) :
  for k in range(tam):
    l4.append(l1[j]+l2[k])

print(l4)