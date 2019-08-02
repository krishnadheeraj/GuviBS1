n,k=input().split()
n=int(n)
k=int(k)
x=[]
s=0
for i in range(n):
  x1=int(input())
  x.append(x1)
for i in range(1,k+1):
  s=s+x[i-1]
print(s)
