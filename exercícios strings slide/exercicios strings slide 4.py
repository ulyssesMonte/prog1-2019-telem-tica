s=""
def entrada(s1):
  s1=input("digite uma frase ")
  return s1

def process(s1):
  s1=s1.replace(" ","#")
  return s1

s=entrada(s)
s=process(s)
print(s)

