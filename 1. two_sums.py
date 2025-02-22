"""
input: nums= [2,7,11,15], target= 9
output = [0,1]
Explaination: becuase nums[0] = 2 and nums[1] = 7, nums[0] + nums[1] == 9, we return [0,1]

"""

class solution:

    def two_sums(self, nums: list[int], target: int)-> list[int]: #hash map
        num_dict ={}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_dict:
                return [num_dict[comp], i]
            num_dict[num] = i
        return []
    
    def two_sums_bf(self, nums, target):#brute force
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum== target:
                    return [i, j]
                
if __name__ == "__main__":
    solution = solution()
    nums = [2,4,5,7,8,9,3]
    output = solution.two_sums_bf(nums=nums, target= 11)
    print(output)
