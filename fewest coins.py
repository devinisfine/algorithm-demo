def fewestcoin(coins,amount):
    arr = [amount+1]*(amount+1)
    arr[0] =0
    for coin in coins:
        for i in range(amount+1):
            if i>=coin:
                arr[i] = min(arr[i],1+arr[i-coin])
    if arr[amount] == (amount+1):
        return -1
    else:
        return arr[amount]

def mostcoin(coins,amount):
    arr = [0]*(amount+1)
    for coin in coins:        
        for i in range(amount+1):
            if i>=coin:
                arr[i] = max(arr[i],1+arr[i-coin])
        if arr[i] == 0:
            return -1
        else:
            return arr[amount]

def madeupways(coins,amount):
    arr = [0]*(amount+1)
    arr[0] =1
    for coin in coins:
        for i in range(amount+1):
            if i>=coin:
                arr[i] = arr[i]+arr[i-coin]
    return arr[amount]
