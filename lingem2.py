up1, up2, up3 = map(int, input("Введите верхние координаты с инвертированными относительно условия знаками: ").split())
down1, down2, down3 = map(int, input("Введите нижние коэфф. как они даны в условии: ").split())
a, b, c, d = map(int, input("Введите коэфф. из уравнения плоскости (их 4): ").split())
for t in range(-10, 10):
    x1 = down1 * t + up1
    y1 = down2 * t + up2
    z1 = down3 * t + up3
    if a * x1 + b * y1 + c * z1 + d == 0:
        dot_A = [x1, y1, z1]
        break
print(dot_A)

for i in range(-10, 10):
    x2 = a * i + up1
    y2 = b * i + up2
    z2 = c * i + up3
    if a * x2 + b * y2 + c * z2 + d == 0:
        dot_C = [x2, y2, z2]
        break
print(dot_C)
print("[", 0-dot_C[0], 0-dot_C[1], 0-dot_C[2], ";", dot_A[0]-dot_C[0], dot_A[1]-dot_C[1], dot_A[2]-dot_C[2], "]")


