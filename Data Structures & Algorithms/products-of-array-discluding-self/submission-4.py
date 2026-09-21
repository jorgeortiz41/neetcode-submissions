class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        full_product = 1
        no_zero_prod = 1
        zeroes = 0

        for i in range(len(nums)):
            full_product *= nums[i]
            if nums[i] == 0:
                zeroes += 1
                full_product = 0
            else:
                no_zero_prod *= nums[i]
                

        for i in range(len(nums)):
            if zeroes > 1:
                result.append(0)
            elif nums[i] == 0:
                result.append(int(no_zero_prod))
            else:
                result.append(int(full_product/nums[i]))

        return result


