import math

def calcular_trajetoria(V0, theta, t):

    theta_rad = math.radians(theta)
    
    g = 9.81 
    
    x = V0 * math.cos(theta_rad) * t

    y = V0 * math.sin(theta_rad) * t - 0.5 * g * t**2    
    return x, y

def main():

V0 = 50  
theta = 45 
t = 2 

x, y = calcular_trajetoria(V0, theta, t)

print(f"Posição horizontal: {x:.2f} metros")
print(f"Altura: {y:.2f} metros")

main()
