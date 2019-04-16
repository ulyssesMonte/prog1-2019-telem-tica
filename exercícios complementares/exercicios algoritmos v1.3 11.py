HT=int(input("digite o total de horas trabalhadas no mês: "))
VH=float(input("digite o valor da hora trabalhada: "))
PD=int(input("digite o percentual de desconto :"))
SB=HT*VH
TD=(PD/100)*SB
SL=SB-TD
print("Horas trabalhadas: ",HT,"\n Salário bruto: ",SB,"\n Desconto: ",TD,"\n Salário líquido: ",SL)


