import math
def minimum_loss(prices,n):
    i=-1
    j=-1
    min_loss = math.inf
    
    for buy_year in range(n):
        for sell_year in range(buy_year+1,n):
            if prices[buy_year] > prices[sell_year]:  
                loss = prices[buy_year] - prices[sell_year]
                if loss < min_loss:
                    i = buy_year
                    j = sell_year
                    min_loss = loss
    if(i==-1):
        print("No loss possible")
    else:
        print(f"Buy in year {i+1}, sell in year {j+1}")

minimum_loss([20,15,7,2,13],5)
        
