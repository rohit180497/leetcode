"""
input: nums= [2,7,11,15], target= 9
output = [0,1]
Explaination: becuase nums[0] = 2 and nums[1] = 7, nums[0] + nums[1] == 9, we return [0,1]

"""

class solution:

    def two_sums(self, nums: list[int], target: int)-> list[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum== target:
                    return [i, j]
                


if __name__ == "__main__":
    solution = solution()
    nums = [2,4,5,7,8,9,3]
    output = solution.two_sums(nums=nums, target= 11)
    print(output)