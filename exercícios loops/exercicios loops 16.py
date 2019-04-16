jog1=0
jog2=0
ponto=0
while (jog1<21) or (jog2<21):
  ponto=int(input("Digite 1 se o jogador 1 fez ponto, ou digite 2 se o jogador 2 fez ponto"))
  if ponto==1:
    jog1+=1
  elif ponto==2:
    jog2+=1
  else:
    print("esse valorr é inválido, tente novamente")

  if jog1==21:
    print("O jogador 1 venceu!")
  elif jog2==21:
    print("O jogador 2 venceu!")
  else:
    print("O Jogo continúa")
