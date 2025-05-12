class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []

        for i, v in enumerate(nums2):
            while stack and v > stack[-1]:
                hashmap[stack[-1]] = v
                stack.pop()
            stack.append(v)

        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                nums1[i] = hashmap[nums1[i]]
            else:
                nums1[i] = -1
        
        return nums1


        