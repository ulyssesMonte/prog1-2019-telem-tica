i=0
media=0
maior=0
menor=1000
while idade != 0:
  idade=int(input("digite a idade: no caso de se digitar 0 o programa encerrará"))
  if idade != 0:
    i+=1
    meida+=idade
    if idade<menor:
      menor=idade
    elif idade>maior:
      maior=idade
print(i,"pessoas, média de idade: ",media/i," maior idade: ",maior," menor idade: ")


