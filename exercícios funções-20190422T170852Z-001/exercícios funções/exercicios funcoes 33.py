def traduzir(lSecreta):
  a=len(lSecreta)
  lt=[]
  for i in range (a):
    if lSecreta[i]==0:
      lt.append(" ")
    elif lSecreta[i]==1:
      lt.append("a")
    elif lSecreta[i]==2:
      lt.append("b")
    elif lSecreta[i]==3:
      lt.append("c")
    elif lSecreta[i]==4:
      lt.append("d")
    elif lSecreta[i]==5:
      lt.append("e")
    elif lSecreta[i]==6:
      lt.append("f")
    elif lSecreta[i]==7:
      lt.append("g")
    elif lSecreta[i]==8:
      lt.append("h")
    elif lSecreta[i]==9:
      lt.append("i")
    elif lSecreta[i]==10:
      lt.append("j")
    elif lSecreta[i]==11:
      lt.append("k")
    elif lSecreta[i]==12:
      lt.append("l")
    elif lSecreta[i]==13:
      lt.append("m")
    elif lSecreta[i]==14:
      lt.append("n")
    elif lSecreta[i]==15:
      lt.append("o")
    elif lSecreta[i]==16:
      lt.append("p")
    elif lSecreta[i]==17:
      lt.append("q")
    elif lSecreta[i]==18:
      lt.append("r")
    elif lSecreta[i]==19:
      lt.append("s")
    elif lSecreta[i]==20:
      lt.append("t")
    elif lSecreta[i]==21:
      lt.append("u")
    elif lSecreta[i]==22:
      lt.append("v")
    elif lSecreta[i]==23:
      lt.append("w")
    elif lSecreta[i]==24:
      lt.append("x")
    elif lSecreta[i]==25:
      lt.append("y")
    elif lSecreta[i]==26:
      lt.append("z")
  return lt