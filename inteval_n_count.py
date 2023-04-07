print("Contagem de números em intervalos predeterminados.\n\nDigite números inteiros e pressione enter.\nO programa aceitará entradas até receber o número 0\n")
n=1
i1=0
i2=0
i3=0
i4=0

while n > 0:
  n=int(input("digite um número:"))

  if n >= 0 and n <= 25 :
    i1 = i1 + 1

  elif n >=26 and n <= 50 :
    i2 = i2 + 1


  elif n >=51 and n <= 75 :
    i3 = i3 + 1

  elif n >=76 and n <= 100 :
    i4 = i4 + 1


print("\nA quantidade de números no intervalo [0,25] é:",i1,"\nA quantidade de números no intervalo [26,50] é:",i2,"\nA quantidade de números no intervalo [51,75] é:",i3,"\nA quantidade de números no intervalo [76,100] é:",i4)