class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # get the length of original list
        lth = len(nums)
        # make a set of the org-list, and get the length of the set
        sLth = len(set(nums))
        # compare the lengths, return true if the same, else false
        return lth != sLth