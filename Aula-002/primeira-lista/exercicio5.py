import math

px = int(input("\nme diga as coordenadas de origem (x e y):\nx = "))
py = int(input("y = "))

dx = int(input("\nagora as coordenas do destino (x e y):\nx = "))
dy = int(input("y = "))

total = (dx - px)**2 + (dy - py)**2

resultado = math.sqrt(total)

print(f"\na distancia linear é de = {resultado:.2f}")

