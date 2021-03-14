#1. Input & Formatting
cases = int(input()) #Number of cases
for case in range(1,cases+1):
    n,k = map(int, input().strip().split()) #using map function to make values N and K into integers N and K
    nums = [int(i) for i in input().strip().split()] #list comprehension to make each value in the array integers
    
    #2. Algorithm
    result = 0 #Number of K countdowns
    count = 0 #Counter to keep track of number of values in current countdown
    for i in range(1, len(nums)):
        #if the current number is 1 less than the previous number, add 1 to the current countdown counter
        if nums[i] == nums[i-1] - 1:
            count += 1
        else:
            #resetting counter if condition is not fufiled 
            count = 0
        
        #Making sure that countdown ends with a one, and that the current countdown includes a K-Countdown
        if nums[i] == 1 and count >= k - 1:
            result += 1

    #3. Output of Result
    print("Case #{}: {}".format(case, result))