class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        next = {}
        stack = []

        for x in nums2:
            while stack and stack[-1]<x:
                next[stack.pop()]=x
            stack.append(x)
        
        for x in stack:
            next[x]=-1
        
        return [next[x] for x in nums1]