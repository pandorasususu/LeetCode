from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sol(num1, num2):
            return int(num2 + num1) - int(num1 + num2)
        
        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(sol))
        return str(int("".join(nums)))
        