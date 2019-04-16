C1=float(input("digite o valor da venda do corretor 1"))
n1=input("digite o nome do corretor 1")
C2=float(input("digite o valor da venda do corretor 2"))
n2=input("digite o nome do corretor 2")
C3=float(input("digite o valor da venda do corretor 3"))
n3=input("digite o nome do corretor 3")
if C1 > 50000.00:
  c1=C1*0.12
elif C1 >= 30000.00:
  c1=C1*0.095
else:
  c1=C1*0.07
if C2 > 50000.00:
  c2=C2*0.12
elif C2 >= 30000.00:
  c2=C2*0.095
else:
  c2=C2*0.07
if C1 > 50000.00:
  c3=C3*0.12
elif C3 >= 30000.00:
  c3=C3*0.095
else:
  c3=C3*0.07
print("Nome: ",n1,", Valor de venda: R$",C1,", comissão: R$",c1)
print("Nome: ",n2,", Valor de venda: R$",C2,", comissão: R$",c2)
print("Nome: ",n3,", Valor de venda: R$",C3,", comissão: R$",c3)

