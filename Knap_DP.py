# Program to implement fractional Knapsack problem

# issue check the profit the answer is not correct for fractional knapsack
def knapsack(items, bagCapacity):

    
    maxProfit = 0

    for key, value in items.items():
     
        weight = value[0]
        profit = value[1]
        ratio = value[2]
           
        print(ratio)
        if (bagCapacity >= weight):
            maxProfit += profit
            bagCapacity -= weight

        else:

            maxProfit += profit * (bagCapacity / weight)
        
    return maxProfit


# append values in dictionary also calculate the profit ratio
def ratioAndValues(weightList, profitList):

    for i in range(len(weightList)):

        weight = weightList[i]
        profit = profitList[i]
        ratio = profit / weight
        items[i] = [weight, profit, ratio]

    return items

# Driver code
weightList = [20, 10, 15, 10]
profitList = [30, 10, 50, 80]
bagCapacity = 40
items = {}

items = ratioAndValues(weightList, profitList)
#  item      weight     profit      ratio
# {0:       [20,        30,         0.6666666666666666]}

# sort the items on the basis of profit ratio
items = dict(sorted(items.items(), key=lambda item: item[1][2], reverse=True))

print(items)
profit = knapsack(items, bagCapacity)
print('profit = ', profit)
