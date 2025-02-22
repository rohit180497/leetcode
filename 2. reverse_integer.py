"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

"""

class solution:

    def reverse(self, num: int) -> int: #brute force using indexing

        sign = -1 if num <0 else 1
        reversed_num = int(str(abs(num))[::-1]) #Python slicing trick works with string, list and tuple

        reversed_num = sign *reversed_num

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num
    
    def reverse_fast(self, num: int):  #using formula modulous

        sign= -1 if num <0 else 1
        reversed_num = 0
        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num = num //10 # to get away with last digit 

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num


                
if __name__ == "__main__":
    solution = solution()
    number = 12345
    output = solution.reverse_fast(number)
    print(output)
