class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        pref = [1]
        suff = [1]*len(nums)
        for i in range(1,len(nums)):
            mult = mult*nums[i - 1]
            pref.append(mult)
        mult = 1
        for i in range(len(nums)-2,-1,-1):
            mult = mult*nums[i + 1]
            suff[i] = mult

        arr = list()
        for i in range(len(nums)):
            arr.append(pref[i]*suff[i])

        return arr
        

        