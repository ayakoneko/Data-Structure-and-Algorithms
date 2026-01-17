class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        heap = []

        for num, f in freq.items():
            heapq.heappush(heap, (f, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for f, num in heap]