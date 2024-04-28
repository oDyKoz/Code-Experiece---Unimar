X1, Y1 = input().split(" ") # inserimos 2 valores em strings, e separamos eles usando o split("")
x1 = float(X1) # transforma o primeiro valor em float
y1 = float(Y1) # transforma o segundo valor em float

X2, Y2 = input().split(" ")
x2 = float(X2)
y2 = float(Y2)

a = ((x2 - x1)**2)
b = ((y2 - y1)**2)
c = a + b
d = c ** 0.5

print(f"{a + b ** 0.5}")

print(f"{c ** 0.5:.4f}")

print(f"{d:.4f}")

print(f"{((x2 - x1)*2 + (y2 - y1)2)*0.5:.4f }")