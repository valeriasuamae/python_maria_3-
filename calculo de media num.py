

nota01=float(input("Digite a nota do PRIMEIRO bimestre: "))
nota02=float(input("Digite a nota do SEGUNDO bimestre: "))
nota03=float(input("Digite a nota do TERCEIRO bimestre: "))
nota04=float(input("Digite a nota do QUARTO bimestre: "))
media = (nota01 + nota02 + nota03 + nota04)/4
print("A nota do 1º Bimestre é: ",nota01)
print("A nota do 2º Bimestre é: ",nota02)
print("A nota do 3º Bimestre é: ",nota03)
print("A nota do 4º Bimestre é: ",nota04)
print("A média final é: ",media)
if media >= 7:
  print("Aprovado")
else:
  print("reprovado")