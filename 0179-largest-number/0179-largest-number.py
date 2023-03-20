from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(y + x) - int(x + y)

        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(compare))
        return str(int("".join(nums)))
        