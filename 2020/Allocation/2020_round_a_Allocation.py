#1. Input & Formatting
cases = int(input()) #Number of cases
for case in range(1, cases+1): #start from 1 as there is no case 0
    houses, budget = input().strip().split() # strip() to get rid of empty space and split() to split the two values, n and b that are on the same line
    # Making values int for easier usage.
    houses = int(houses)
    budget = int(budget)
    costs = [int(cost) for cost in input().strip().split()] #same formatting here, just using list comprehension to save time, which is very valuable in competitive programming
    
    #2. Algorithm
    costs.sort() #Sorting house prices form low to high
    result = 0
    for cost in costs:
        #while the budget can still afford the house, it is paid for and deducted from the budget
        #for loop is terminated once budget can no longer afford the next house, which is the cheapest in all the remaining houses
        if budget >= cost: 
            budget = budget - cost
            result += 1
        else:
            break
        
    #3. Output of Result
    print("Case #{}: {}".format(case, result))