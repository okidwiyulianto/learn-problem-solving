# Diketahui:
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [nums[0]]
        for i in range(1, len(nums)):
            # Hitung running sum dengan menambahkan elemen saat ini dengan running sum sebelumnya
            result.append(result[i - 1] + nums[i])
        
        return result