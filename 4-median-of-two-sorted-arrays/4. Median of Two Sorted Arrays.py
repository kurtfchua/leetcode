class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i]<=nums2[j]:
                merged_nums.append(nums1[i])
                i+=1
            else:
                merged_nums.append(nums2[j])
                j+=1
        merged_nums.extend(nums1[i:])
        merged_nums.extend(nums2[j:])

        if len(merged_nums) % 2 != 0:
            median = len(merged_nums)//2
            return float(merged_nums[median])
        else:
            medians = len(merged_nums)//2, (len(merged_nums)//2) - 1
            avg = (merged_nums[medians[0]]+merged_nums[medians[1]])/2
            return avg



            
        