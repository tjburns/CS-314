# TODO add error checking for matrices that cannot be multiplied
#   then exit

line = input().split()
rows1 = int(line[0])
columns1 = int(line[1])
mat1 = [[float(0.0) for j in range(columns1)] for i in range(rows1)]
for i in range(rows1):
    line = input().split()
    for j in range(columns1):
        mat1[i][j] = float(line[j])

line = input().split()
rows2 = int(line[0])
columns2 = int(line[1])
mat2 = [[float(0.0) for j in range(columns2)] for i in range(rows2)]
for i in range(rows2):
    line = input().split()
    for j in range(columns2):
        mat2[i][j] = float(line[j])

if columns1 != rows2:
    print("invalid input")
else:

    """
    for i in range(rows):
        for j in range(columns):
            print(mat1[i][j])
    """

    matmult = [[0 for j in range(columns2)] for i in range(rows1)]
    """
    for i in range(rows1):
        for j in range(columns2):
            print(matmult[i][j])
    """

    for i in range(rows1):
        for j in range(columns2):
            for k in range(rows2):
                matmult[i][j] += mat1[i][k] * mat2[k][j]

    for i in range(rows1):
        for j in range(columns2):
            print(matmult[i][j])