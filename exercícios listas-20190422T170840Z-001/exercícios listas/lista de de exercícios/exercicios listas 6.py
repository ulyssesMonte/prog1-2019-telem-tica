n1=[],n2=[],n3=[],n4=[],m=[],am=0
for i in range (10):
  n1.append(float(input("digite a nota1 do aluno ",i)))
  n2.append(float(input("digite a nota2 do aluno ",i)))
  n3.append(float(input("digite a nota3 do aluno ",i)))
  n4.append(float(input("digite a nota4 do aluno ",i)))
  m.append((n1[i]+n2[i]+n3[i]+n4[i])/4)
  if m[i]>7.0:
    am+=1
print(am)
