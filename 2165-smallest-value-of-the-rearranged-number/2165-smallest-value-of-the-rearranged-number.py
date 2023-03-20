class Solution:
    def smallestNumber(self, num: int) -> int:
        smallest = True
        if num == 0:
            return 0
        if num < 0:
            num = abs(num)
            smallest = False
        
        nums_list = list(map(int, str(num).strip()))
        nums_set = set(nums_list)
        try:
            nums_set.remove(0)
        except:
            pass
        min_num, max_num = min(nums_set), max(nums_set)
        min_list, max_list = nums_list[:], nums_list[:]
        min_list.remove(min_num)
        max_list.remove(max_num) 
        min_list, max_list = list(map(str, min_list)), list(map(str, max_list))
        
        print(nums_list, nums_set, min_num, max_num, min_list, max_list)
        
        def compare_smallest(num1, num2):
            return int(num1 + num2) - int(num2 + num1)
        
        def compare_biggest(num1, num2):
            return int(num2 + num1) - int(num1 + num2)
        
        if smallest:
            min_list.sort(key=functools.cmp_to_key(compare_smallest))
            print(min_list)
            return int(str(min_num) + ''.join(min_list)) 
        else:
            max_list.sort(key=functools.cmp_to_key(compare_biggest))
            print(max_list)
            return -int(str(max_num) + ''.join(max_list))
        
    