def solve(A, k):
    vis = [0]*((len(A)) + k)
    for i in A:
        if i >= len(vis):
            continue
        vis[i]=1
    cnt = 0
    ans = 0
    for i in range (len(vis)):
        if vis[i]==0:
            cnt+=1
            if cnt==k:
                ans = i
                break
    return ans

A = [7, 5, 7, 1]
k = 3
print(solve(A, k))