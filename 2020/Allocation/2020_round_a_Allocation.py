cases = int(input())
for case in range(1, cases+1):
    houses, budget = input().strip().split()
    houses = int(houses)
    budget = int(budget)
    costs = [int(cost) for cost in input().strip().split()]
    costs.sort()
    result = 0
    for cost in costs:
        if budget >= cost:
            budget = budget - cost
            result += 1
        else:
            break
    print("Case #{}: {}".format(case, result))