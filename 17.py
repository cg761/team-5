a=int(input())
v=list(map(int,input().split()))
c=int(input())
count=0

for i in range(c):
    s=0
    su=0
    g,f=map(int,input().split())
    for j in range(g-1,f):
        if v[j]%2==0 or v[j]%3==0 or v[j]%5==0 or v[j]%7==0:
            s=s+v[j]
        for k in range(g-1,f):
            su=su+v[k]
    print(su-s+2)
'''
        for k in range(2,v[j]+1,1):
            if v[j]%k==0:
                count=count+1
                #print(v[j], k, count)
        if count==1:
            s=s+v[j]
        count=0
            
    print(s)
'''
'''
a=int(input())
b=0
for i in range(2,a+1):
  if a%i==0:
    b=b+1
if b==1:
  print("prime")
else:
  print("not prime")
  '''
