#1. Input & Formatting
T = int(input()) #T test cases
for t in range(1, T + 1):
    n = int(input()) # Integer N
    out = 0 #number of peaks
    checkpoints = list(map(int,input().strip().split())) #using map function, making each value in the list to be an integer
    
    #2. Algorithm
    for i in range(1, n-1):
        #checking if the current checkpoint at index i is higher than the previous checkpoint and also the next checkpoint
        if checkpoints[i] > checkpoints[i-1] and checkpoints[i] > checkpoints[i+1]:
            out += 1
    
    #3. Ouput of Result
    print("Case #{0}: {1}".format(t,out))