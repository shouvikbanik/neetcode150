from heapq import heapify, heappop, heappush


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        heapify(nums)
        self.nums = nums
        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]
