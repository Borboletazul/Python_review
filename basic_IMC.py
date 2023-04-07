#Beginner useful functions
#variable_float/print/input/math_operates/if/elif/else/condit_parameters._<=_<

print("Calculo IMC")
a = float(input("digite sua altura em metros(ex.:1.70):"))
p = float(input("digite seu peso em Kg:"))
IMC = p/a**2
print("IMC:",IMC)
if IMC<20.7:
  print("Condição: Abaixo do peso")
elif 20.7<=IMC<=27.8:
  print("Condição: Peso normal")
elif 27.8<IMC<=31.1:
  print("Condição: Acima do peso")
else:
  print("Condição: Obesidade")
