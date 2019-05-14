def separar(s): #minha versão do split
  s=s+" "
  x=" "
  l=[]
  a=0
  for i in range(len(s)):
    if (s[i]==x)or(i==len(s)):
      l.append(s[a:i])
      a=i+1
  return l

def contar(s): #minha versão do len
  i=-1
  for j in s:
    i+=1
  return i

def AAA(s): #MINHA VERSÃO DO UPPER
  S=""
  for i in s:
    if i =="a":
      S=S+"A"
    elif i =="b":
      S=S+"B"
    elif i =="c":
      S=S+"C"
    elif i =="d":
      S=S+"D"
    elif i =="e":
      S=S+"E"
    elif i =="f":
      S=S+"F"
    elif i =="g":
      S=S+"G"
    elif i =="h":
      S=S+"H"
    elif i =="i":
      S=S+"I"
    elif i =="j":
      S=S+"J"
    elif i =="k":
      S=S+"K"
    elif i =="l":
      S=S+"L"
    elif i =="m":
      S=S+"M"
    elif i =="n":
      S=S+"N"
    elif i =="o":
      S=S+"O"
    elif i =="p":
      S=S+"P"
    elif i =="q":
      S=S+"Q"
    elif i =="r":
      S=S+"R"
    elif i =="s":
      S=S+"S"
    elif i =="t":
      S=S+"T"
    elif i =="u":
      S=S+"U"
    elif i =="v":
      S=S+"V"
    elif i =="w":
      S=S+"W"
    elif i =="x":
      S=S+"X"
    elif i =="y":
      S=S+"Y"
    elif i =="z":
      S=S+"Z"
  return S

def aaa(S): #minha versão do lower
  s=""
  for i in S:
    if i =="A":
      s=s+"a"
    elif i =="B":
      s=s+"b"
    elif i =="C":
      s=s+"c"
    elif i =="D":
      s=s+"d"
    elif i =="E":
      s=s+"e"
    elif i =="F":
      s=s+"f"
    elif i =="G":
      s=s+"g"
    elif i =="H":
      s=s+"h"
    elif i =="I":
      s=s+"i"
    elif i =="J":
      s=s+"j"
    elif i =="K":
      s=s+"k"
    elif i =="L":
      s=s+"l"
    elif i =="M":
      s=s+"m"
    elif i =="N":
      s=s+"n"
    elif i =="O":
      s=s+"o"
    elif i =="P":
      s=s+"p"
    elif i =="Q":
      s=s+"q"
    elif i =="R":
      s=s+"r"
    elif i =="S":
      s=s+"s"
    elif i =="T":
      s=s+"t"
    elif i =="U":
      s=s+"u"
    elif i =="V":
      s=s+"v"
    elif i =="W":
      s=s+"w"
    elif i =="X":
      s=s+"x"
    elif i =="Y":
      s=s+"y"
    elif i =="Z":
      s=s+"z"
  return s

def troca(s,o,t) :    #minha versão do replace, o s é a string, o "o" é  o valor a ser  substituido e o t é o valor que irá substituir
  l=[]
  f=""
  for i in range(len(s)):
    l.append(s[i])
  for i in range(len(l)):
    if l[i]==o:
      l[i]=t
  for i in range(len(l)):
    f=f+l[i]
  return f