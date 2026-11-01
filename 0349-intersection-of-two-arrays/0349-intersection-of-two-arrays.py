class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set(nums1)
        ans = []
        for i in nums2:
            if i in seen:
                ans.append(i)
                seen.remove(i)
        return ans 
        