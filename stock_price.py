# Best time to buy and sell stock 

#input = [7,1,5,3,6,4]
#output = 5
#Explaination: Buy on day 2 (price=1) and sell on day 5 (price= 6), profit = 6-1 = 5

class solution:

    def max_profit(self, prices: list[int]):
        min_price = float('inf')    # bcoz we are going to compare this price with all the items we can't keep 0 otherwise min price will be 0
        max_profit = 0  #this we can keep as zero 
        for price in prices:
            min_price = min(min_price, price)       #so here min price will be constantly 1 as in the list it will compare with all other elemnets
            print("min price:" , min_price)
            max_profit = max(max_profit, price - min_price)
            print("max profit:", max_profit)
        return max_profit
    


if __name__ == "__main__":
        # Create an instance of the Solution class
        solution = solution()
        prices = [7,1,5,3,6,4]
        print(solution.max_profit(prices))


