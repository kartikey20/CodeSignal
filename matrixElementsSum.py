def matrixElementsSum(matrix):
    rowLen = len(matrix)
    colLen = len(matrix[0])
    haunted = [[False for _ in range(colLen)] for i in range(rowLen)]
    sum = 0
    for row in range(rowLen):
        for col in range(colLen):
            if matrix[row][col] == 0:
                haunted[row][col] = True
                for i in range(row, rowLen):
                    haunted[i][col] = True
            else:
                if haunted[row][col] == False:
                    sum += matrix[row][col]
    return sum
