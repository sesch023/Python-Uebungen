import math

a = float(input("Bitte geben Sie ihr a an: "))

if a == 0:
    print("Keine gültige Lösung für a = 0!")
    exit(0)

b = float(input("Bitte geben Sie ihr b an: "))
c = float(input("Bitte geben Sie ihr c an: "))

sqrt_num = b**2.0 - 4.0*a*c

if sqrt_num < 0:
    print("Keine Lösung vorhanden!")
    exit(0)

sqrt_num = math.sqrt(sqrt_num)
x1 = (-b + sqrt_num) / 2.0*a
x2 = (-b - sqrt_num) / 2.0*a

if x1 == x2:
    print("Eine Lösung vorhanden: " + str(x1))
else:
    print(f"Zwei Lösungen vorhanden: {str(x1)}, {str(x2)}")
