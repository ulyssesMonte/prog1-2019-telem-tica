n1=int(input("digite um número"))
n2=int(input("digite outro número"))
n3=int(input("digite outro número"))
maior=0
menor=0
if n1>n2:
  maior=n1
  menor=n2
else: 
  maior=n2
  menor=n1
if n3>maior:
  maior=n3
elif menor>n3:
  menor=n3
print("O maior número é: ", maior, "\n e o menor é: ", menor)


