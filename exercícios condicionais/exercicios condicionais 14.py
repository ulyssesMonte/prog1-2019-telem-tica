cpf=int(input("digite seu cpf"))
nome=input("digite seu nome")
rend=float(input("rendimento anual"))
impret=float(input("imposto retido na fonte"))
contr=float(input("contribuição previdenciária"))
desp=float(input("despesas médicas"))
depen=int(input("número de dependentes"))

cadadepen=1080.00
depenDED=depen*cadadepen
totalDED=contr+desp+depenDED

basecalc = rend-totalDED

impdev=0.0

imposto=0.0

if (basecalc > 10800.00) and (basecalc < 21600.00) :
  impdev = (basecalc * (basecalc*0.15))-1620.00
elif (basecalc > 21600.00):
  impdev = (basecalc * (basecalc*0.25))-3780.00
else:
  impdev = basecalc

imposto=impdev-impret

if (imposto>0)
  print("imposto a pagar: ", imposto)
else:
  print("imposto a ser restituido: ", imposto*-1)
  
print("CPF: ", cpf, "\n Nome: ", nome, "\n Rendimento anual: ", rend, "\n Imposto retido na fonte: ", impret, "\n Contribui��o previdenci�ria: ", contr,"\n Despesas m�dicas: ", desp, "\n N�mero de dependentes: ",depen,"\n � deduzido para cada dependente um valor de: ", cadadepen, "\n C�lculo do valor total das dedu��es: ", totalDED, "\n Base de c�lculos: ", basecalc, "\n Imposto devido: ", impdev,)