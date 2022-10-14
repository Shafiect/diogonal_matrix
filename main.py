import numpy as np

m = int(input())
n = int(input())

a = np.full((m,n),0)

k = 1
for r in range(m):
  c = 0
  while r>=0 and c<=n-1:
    a[r][c] = k
    k = k+1
    r = r-1
    c = c+1    


for c in range(1,n):
  r = m-1
  while c<=n-1 and r>=0:
    a[r][c] = k
    k = k+1
    r = r-1
    c = c+1
   
print(a)
  
