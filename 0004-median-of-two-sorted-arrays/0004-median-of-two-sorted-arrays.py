class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        num = nums1 + nums2
        num.sort()

        s=len(num)//2

        if len(num) % 2 != 0:
            return num[s]
        else:
            med=(num[s-1]+num[s])/2
            return med