class Solution(object):
    def subarraySum(self, nums, k):
        prefix = 0
        count = {0: 1}
        ans = 0

        for num in nums:
            prefix += num

            if prefix - k in count:
                ans += count[prefix - k]
            
            count[prefix] = count.get(prefix, 0) +1
            
        return ans        