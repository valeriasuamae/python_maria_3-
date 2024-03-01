def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def verifica_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def main():
    lado1 = float(input("Digite o primeiro lado do triângulo: "))
    lado2 = float(input("Digite o segundo lado do triângulo: "))
    lado3 = float(input("Digite o terceiro lado do triângulo: "))

    if verifica_triangulo(lado1, lado2, lado3):
        tipo = tipo_triangulo(lado1, lado2, lado3)
        print(f"Os lados formam um triângulo {tipo}.")
    else:
        print("Os valores não podem formar um triângulo.")

    if name == " main ":
       main()