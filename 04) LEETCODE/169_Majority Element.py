class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        len_nums = len(nums)
        
        return nums[len_nums//2]