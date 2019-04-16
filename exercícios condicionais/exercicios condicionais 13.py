nome=input("Nome: ")
tipoapt=input("Tipo de apartamento ultilizado: A, B, C ou D: ")
diarias=int(input("Número de diárias: "))
consu=float(input("Valor de consumo interno do hóspede: "))
diaria=0.0
totaldiaria=0.0
subtotal-0.0
taxa=0.0
totalgeral-0.0
if tipoapt.upper =="A":
  diaria=150.00
elif tipoapt.upper=="B"
  diaria=100.00
elif tipoapt.upper=="C"
  diaria=75.00
elif tipoapt.upper=="D"
  diaria=50.00
else:
  print("Valor inválido")

totaldiaria=diaria*diarias
subtotal=totaldiaria + consu
taxa=subtotal*0.1
totalgeral=subtotal+taxa

print("Nome: ",nome,"\n Tipo de apartamento: ",tipoapt,"\n Número de diárias utilizadas: ",diarias,"\n Valor unitário da diária: ",diaria,"\n valor toal das diárias: ", totaldiaria,"\n Consumo interno: ",consu,"\n Subtotal",subtotal,"\n Valor da taxa de serviço: 10% \n Total Geral: ",totalgeral)