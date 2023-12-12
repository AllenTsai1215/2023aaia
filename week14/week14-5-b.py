a=list(map(int,input().split()))
ans=0
n=len(a)
for i in range(n-2):
	if a[i]==a[-1]:
		ans+=1
print(ans)