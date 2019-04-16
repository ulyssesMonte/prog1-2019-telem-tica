n=int(input("digite um número: "))
fibo=0
a=0
b=1
print(a)
print(b)
for i in range(3,n+1,1):
  fibo=a+b
  print(fibo)
  a=b
  b=fibo
