T = int(input())
for t in range(1, T + 1):
    n = int(input())
    out = 0
    l = list(map(int,input().split()))
    for i in range(1, n-1):
        if l[i] > l[i-1] and l[i] > l[i+1]:
            out += 1
    print("Case #{0}: {1}".format(t,out))