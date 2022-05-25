def dfs_matrix(matrix):
    
    def dfs(i, j):
        if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]) or matrix[i][j] != "1":
            return

        matrix[i][j] = "."
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "1":
                dfs(i,j)
                count += 1

    return count
