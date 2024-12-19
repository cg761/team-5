a=int(input())
q=0
q=int(q)
b=0
b=int(b)
v=list(map(int,input().split()))
c=int(input())
for i in range(0,c,1):
  g,f=map(int,input().split())
  q=0
  for j in range(g,f,1):
    for z in range(1,v[j],1):
      if v[j]%z==0:
        b=b+1
      if b==1:
        q=q+int(v[j])
  print(q)
