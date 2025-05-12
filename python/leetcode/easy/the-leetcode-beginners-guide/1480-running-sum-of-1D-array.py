# Diketahui:
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

# Ditanya: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

# Batasan:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6


# Dijawab:
        # Inisialisasi list hasil dengan elemen pertama dari nums
        result = [nums[0]]
        
        # Iterasi dari elemen kedua hingga terakhir
        for i in range(1, len(nums)):
            # Hitung running sum dengan menambahkan elemen saat ini dengan running sum sebelumnya
            result.append(result[i - 1] + nums[i])
        
        return result

# Penjelasan:
# for i in range(1, len(nums)): artinya, kita membuat perulangan dari elemen yang mulai start dari 1 dan berhenti di elemen terakhir dari list nums.
# result.append(result[i - 1] + nums[i]) artinya, kita menambahkan elemen saat ini dengan running sum sebelumnya.
# return result artinya, kita mengembalikan hasil akhir dari list result.