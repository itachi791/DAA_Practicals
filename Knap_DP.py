# Program to implement 0-1 knapsack using DP

profit = [0, 1, 2, 5, 6]  
weight = [6, 2, 3, 4, 5]  
bagCapacity = 8  
n = len(profit) - 1 

table = [[0] * (bagCapacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1): 
    for w in range(1, bagCapacity + 1):  
        if weight[i] <= w:
          
            table[i][w] = max(profit[i] + table[i-1][w - weight[i]], table[i-1][w])
        else:
           
            table[i][w] = table[i-1][w]

print(table[n][bagCapacity])

i = n
j = bagCapacity
while (i > 0 and j > 0) :

    if (table[i][j] == table[i-1][j]):
        print(i , " = 0")
        i = i - 1
    else:
        print(i, "= 1")
        i = i - 1
        j = j - weight[i]

print(table)
