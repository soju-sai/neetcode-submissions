class Solution:
    def isPalindrome(self, s: str) -> bool:
        begin = 0
        last = len(s)-1

        # recursive case:
        # 開頭大於或等於結尾的指標就結束
        # base case:
        # 開頭和結尾不同就return False
        while begin < last:
            # 碰到非non-alphanumeric就平移ㄧ格
            if not s[begin].isalnum():
                begin += 1
                continue
            if not s[last].isalnum():
                last -= 1
                continue
            print(s[begin], s[last])
            if s[begin].lower() != s[last].lower():
                return False
            
            # 比較開頭和結尾，相同就都平移ㄧ格
            begin += 1
            last -= 1
        
        return True