entrada = input().split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

pi = 3.14159

area_do_triangulo_retangulo = (A * C) / 2
area_do_circulo = pi * (C * C)
area_do_trapezio = ((A + B) * C) / 2 # : Área = ((Base Maior + Base Menor) x Altura) / 2
area_do_quadrado = B * B
area_do_retangulo = A * B

print(f"TRIANGULO: {area_do_triangulo_retangulo:.3f}")
print(f"CIRCULO: {area_do_circulo:.3f}")
print(f"TRAPEZIO: {area_do_trapezio:.3f}")
print(f"QUADRADO: {area_do_quadrado:.3f}")
print(f"RETANGULO: {area_do_retangulo:.3f}")

