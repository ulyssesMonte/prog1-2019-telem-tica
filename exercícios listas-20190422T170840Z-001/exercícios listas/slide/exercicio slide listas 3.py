l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
l3=[]
l4=[]
tam=4
for i  in range(tam+1) :
  l3.append(l1[i]+l2[i])
for j in range(tam,-1,-1) :
  l4.append(l3[j])
  
print(l4)
print(l3)
