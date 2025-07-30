class Solution:
    def summaryRanges(self,nums):
        if not nums:
            return []
        new_list = []
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                end = nums[i-1]
                if start == end:
                    new_list.append(str(start))
                else:
                    new_list.append(f"{start}->{end}")
                start = nums[i]
        end = nums[-1]
        if start == end:
            new_list.append(str(start))
        else:
            new_list.append(f"{start}->{end}")
        return new_list
    
nums = list(map(int,input().split()))
obj = Solution()
print(obj.summaryRanges(nums))