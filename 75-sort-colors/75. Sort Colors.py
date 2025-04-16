class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums)-1)

    def quick_sort(self, arr, start, end):
        if start >= end: 
            return arr
        
        pivot = arr[end]
        j = start

        for i in range(start, end):
            if arr[i] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1

        arr[j], arr[end] = arr[end], arr[j]
        
        self.quick_sort(arr, start, j-1)
        self.quick_sort(arr, j+1, end)

        return arr
        