s=input("digite seu nome ")
s1=""
j=len(s)
for i in range(j+1):
  for k in range(i):
    s1+=s[k]
  print(s1)
  s1=""
  

