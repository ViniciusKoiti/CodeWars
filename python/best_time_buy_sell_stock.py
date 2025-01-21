def best_time_buy_sell_stock(arr):
    min_price = float('inf')
    max_price = 0
    
    for i in range(len(arr)):
        if i < min_price:
            min_price = i
    profit = i - min_price
    
    if profit > max_price:
        max_price  = profit
    return max_price
           
test_cases = {
    "Test 1": [7, 1, 5, 3, 6, 4],  
    "Test 2": [7, 6, 4, 3, 1],      
    "Test 3": [1, 2, 3, 4, 5],      
    "Test 4": [2, 4, 1],          
    "Test 5": [3, 2, 6, 5, 0, 3],  
} 

results = {key: best_time_buy_sell_stock(value) for key, value in test_cases.items()}
print(results)