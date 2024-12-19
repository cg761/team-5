a=int(input())
b=0
for i in range(2,a+1):
  if a%i==0:
    b=b+1
if b==1:
  print("prime")
else:
  print("not prime")
