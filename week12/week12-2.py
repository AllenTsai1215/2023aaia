a=list(map(int,input().split()))
#print(sum(a)-a[0])
ans=0
n=a[0]
for i in range(1,n+1):
	ans+=a[i]
print(ans)