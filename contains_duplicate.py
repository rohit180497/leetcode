"""
given an array nums, return trur if any value appears at least twice in the array
input = [1,2,3,1]
output = true

1. check all cases
2. sorting
3. set

"""

class solution:

    def duplicate(self, nums: list[int]):
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True

    

if __name__ == "__main__":
    solution = solution()
    arr1 = [1,2,3,4,5,1]
    print(solution.duplicate(arr1))