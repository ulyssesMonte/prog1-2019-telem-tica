nome=input("digite o nome: ")
salario=float(input("digite o salário: "))
reajuste=0.0

if salario < 1000.00 :
  reajuste=salario*0.2
elif (salario > 1000.00) and (salario < 5000.00):
  reajuste=rslario*01
elif (salário > 5000.00):
  
else:
  print("valor inválido")
 print("Nome: ", nome, "\n Saláário atual: ", salario, "\n salário rreajustado: ", salario+reajuste)
