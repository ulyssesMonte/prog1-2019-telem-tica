maior=0.0
media=0.0
poste=0
for i in range (0,20):
  alt=float(input("digite a altura: "))
  if alt>maior:
    maior=alt
  media+=alt
  if alt>2.0:
    poste+=1
print("maior, média, e numero de pessoas com mais de 2m de altura :",maior," ",media/20," ",poste)


