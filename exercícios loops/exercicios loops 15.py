numand=int(input("Digite o número de andares do prédio"))
numpes=0
nument=0
numsai=0
for i in range (0:numand+1)
  print("Quantas pessoas entraram no elevador no ",i,"° andar?")
  nument=int(input())
  numsai=int(input("Quantas pessoas sairam do elevador no ",i,"°andar"))
  numpes+=nument
  numpes-=numsai
  if numpes>15:
    print("devem sair do elevador ",numpes-15,"pessoas")
print("restaram no elevador para desscer ",numpes,"pessoas")

