class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 想法：
        # heights bar數量小於2無法比較，回傳0
        # 一定要有兩個bar，所以從i=1開始迴圈
        # 存第一高bar的資訊（index, height）
        # 目前容積 i height * (i index - 1st index)
        # 目前最大容積和目前容積比較，更新最大資訊，第二高bar的資訊
        # 存目前最大容積，2nd height * |(1st position - 2nd position)|絕對值
        # 存第二高bar的資訊
        # 最後回傳最大容積
        # if len(heights) < 2:
        #     return 0
        
        # highest = [0, heights[0]]
        # sec_high = [1, heights[1]]
        # if highest[1] < sec_high[1]:
        #     highest, sec_high = sec_high, highest
        # max_amount = sec_high[1] * abs(sec_high[0] - highest[0])
        # for i in range(2, len(heights)):
        #     # 容積：2nd hight * |(2nd index - 1st index)|
        #     current_amount = min(heights[i], highest[0]) * (i - highest[0])
        #     print("i:", i)
        #     print("current:", current_amount, min(heights[i], highest[1]))
        #     print("highest:", highest)
        #     # current_amount = heights[i] * (i - min(sec_high[0], highest[0]))
        #     if current_amount > max_amount:
        #         max_amount = current_amount
        #         sec_high = [i, heights[i]]

        #         highest = [i, heights[i]] if heights[i] > highest[1] else highest
        #     print("max:", max_amount, highest)

        # 解法：
        # 從最左和最右往內收斂，取得最大容積
        # 小的那邊逐漸往內收斂
        l, r = 0, len(heights)-1
        max_amount = 0
        while l < r:
            amount = min(heights[l], heights[r]) * (r - l)
            if amount > max_amount:
                max_amount = amount
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_amount
                