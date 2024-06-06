"""
Aim:
i/p= [0,1,0,3,12,4]
o/p : [1,3,12,4,0,0]

"""

class solution:
    def moveZero(self, nums:list[int]):

        prev_indx = 0    #counter for previous index
        for i in range(len(nums)):
            if nums[i]!=0:          #checking if no. is not zero then we need to swap
                nums[i], nums[prev_indx] = nums[prev_indx], nums[i] #swap here
                prev_indx +=1 #increment previous index

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = solution()
    
    # Test the moveZeroes method
    nums = [1, 2, 3, 0, 0, 9, 0]
    solution.moveZero(nums)
    print(nums)
    
