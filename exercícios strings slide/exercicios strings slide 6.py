def orde(l):
  for i in range (len(l)):
    for j in range (len(l)):
      if l[i] < l[j]:
        l[i], l[j] = l[j], l[i]
  return l

def conv(s):
  l=[]
  for i in range(len(s)):
    l.append(s[i])
  return l

s1=input("digite a primeira palavra ")
s2=input("digite a segunda palavra ")
if (s1==s2):
  print("as duas palavras j� s�o iguais")
elif (orde(conv(s1))==orde(conv(s2))):
  print(s1," � um anagrama de ",s2)
else:
  print("n�o se trata de um anagrama")

)