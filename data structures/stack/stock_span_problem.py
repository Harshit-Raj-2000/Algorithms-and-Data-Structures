# The span Si of the stock’s price on a given day i is defined as the maximum number 
# of consecutive days just before the given day, for which the price of the stock 
# on the current day is less than or equal to its price on the given day. 

# {100, 80, 60, 70, 60, 75, 85}
# {1, 1, 1, 2, 1, 4, 6}

# stock_span(ith element) = 1 + stock_span(i-1th element) + no.of previous elements samller


def calculate_span(prices):
    output = []
    stack = []

    stack.append(0)
    output.append(1)

    for i in range(1, len(prices)):

        while len(stack) != 0 and prices[i] >=prices[stack[-1]]:
            stack.pop()
        
        output.append( i+1 if len(stack) == 0 else (i - stack[-1] ))

        stack.append(i)
    
    return output

price = [10, 4, 5, 90, 120, 80]
print(calculate_span(price))
