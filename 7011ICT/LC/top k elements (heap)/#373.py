class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2 or k == 0:
            return []

        n1, n2 = len(nums1), len(nums2)
        heap = []
        res = []

        for i in range(min(k, n1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(res) < k:
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res