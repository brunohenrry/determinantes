matrix = [[1, 2, 3], [2, 5, 6], [2, 5, 8]]

a = matrix[0][0]
b = matrix[0][1]
c = matrix[0][2]
d = matrix[1][0]
e = matrix[1][1]
f = matrix[1][2]
g = matrix[2][0]
h = matrix[2][1]
i = matrix[2][2]

principal = a*e*i + b*f*g + c*d*h
secundaria = c*e*g + a*f*h + b*d*i

determinant = principal - secundaria

print("Determinante da matriz de ordem 3:", determinant)
