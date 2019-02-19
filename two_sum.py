def find(nums,value):
    l=[]
    for i in range(len(nums)):
        if nums[i]==value:
            l.append(i)
    return l

class Solution(object):    
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            x=target-nums[i]
            if x in nums[i+1:len(nums)]:
                if x==nums[i]:
                    y=find(nums,x)
                else:
                    y=[i,find(nums,x)[0]]
                return y


s=Solution()
s.twoSum([3,3],6)
s.twoSum([3,2,4],6)
s.twoSum([2,7,11,15],9)
s.twoSum([-1,-2,-3,-4,-5],-8)
