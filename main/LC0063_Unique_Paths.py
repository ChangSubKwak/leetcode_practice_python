class LC0063_Unique_Paths:
  def uniquePaths(self, m: int, n: int) -> int:
    row, col = (m, n)
    count = [[0] * col] * row
    count[0] = [1 for i in range(col)]

    for i in range(row):
      count[i][0] = 1

    for i in range(1, row):
      for j in range(1, col):
        count[i][j] = count[i - 1][j] + count[i][j - 1]

    return count[m - 1][n - 1]
