#SOIT1018_ADVANCE_004
a=int(input())
ans=0
for i in range(1,a+1):
	ans+=i*10+i
print(ans,end='')