def knapsack(profit, weight, capacity):
  N, M = len(profit), capacity
  dp = [[0] * (M + 1) for _ in range(N)]
  
  for i in range(N):
    dp[i][0] = 0
  for c in range(M + 1):
    if weight[0] <= c:
      dp[0][c] = profit[0]
     
  for i in range(N):
    for c in range(M + 1):
      skip = dp[i-1][c]
      include = 0
      if c - weight[i] >= 0:
        include = profit[i] + dp[i-1][c-weight[i]]
      dp[i][c] = max(skip, include)
  return dp[N-1][M]
     
