class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        pre_list = [None] * len(nums)
        for i in range(len(nums)):
            pre_list[i] = prefix
            prefix *= nums[i]
        # print(pre_list)

        postfix = 1
        post_list = [None] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            post_list[i] = postfix
            postfix *= nums[i]
        # print(post_list)
        
        res = []
        for i in range(len(nums)):
            res.append(pre_list[i] * post_list[i])

        return res
            