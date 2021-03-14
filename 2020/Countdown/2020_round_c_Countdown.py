cases = int(input())
for case in range(1,cases+1):
    n,k = input().strip().split()
    n = int(n)
    k = int(k)
    nums = [int(i) for i in input().strip().split()]
    result = 0
    count = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] - 1:
            count += 1
        else:
            count = 0
        if nums[i] == 1 and count >= k - 1:
            result += 1
            
    print("Case #{}: {}".format(case, result))