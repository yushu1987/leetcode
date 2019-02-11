#https://leetcode-cn.com/problems/next-greater-element-i/
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = {}
        l = len(nums)
        for k,v in enumerate(nums):
            if k == l -1:
                stack[v] = -1
                break
            for j in nums[k+1:]:
                if j> v and (v not in stack or stack[v] == -1):
                    stack[v] = j
                    break
                else:
                    stack[v] = -1
        print stack, findNums
        return [stack[k] for k in findNums]
