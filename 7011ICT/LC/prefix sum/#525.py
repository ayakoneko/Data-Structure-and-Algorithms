class Solution(object):
    def findMaxLength(self, nums):
        prefix = 0
        first = {0: -1}
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in first:
                ans = max(ans, i-first[prefix])
            else:
                first[prefix] = i

        return ans        