a{"cpf":0,
  "nome":"",
  "idade":0,
  "telefone"0}
x=True
while x==True:
  print("Criando novo cadastro...")
  a["cpf"]=int(input("Digite o cpf "))
  a["nome"]=input("Digite o nome ")
  a["idade"]=int(input("Digite a idade "))
  a["telefone"]=int(input("Digite o telefone "))
  l.append(a)
  y=input("Deseja cadastrar mais alguém? s/n ")
  if y.lower()=="s":
    pass
  else:
    x=False
print("preparando-se para exibir a agenda...")
for i in range(len(l)):
  print("CPF: ",l[i]["cpf"],"\n","NOME:: ",l[i]["nome"],"\n","IDADE: ",l[i]["idade"],"\n","TELEFONE: ",l[i]["telefone"],"\n",)