def remov_nb(n):
    
    c = []
    
    z = n * (n + 1) / 2
    
    for i in range(1, n + 1):
        j = (z - i) / (i + 1)
        if j%1 == 0 and j <= n + 1 and i != j:
            c.append((i, j))
    return c
    
Complexity:
  Time: O(N)
  Space: O(N)
