class Solution:

    def encode(self, strs: List[str]) -> str:
        # # pseudo:
        # # 把每個character轉成ascii，會落在ord(0)到ord(255)之間
        # # 每個字串的分隔字元用ord('300')處理

        # encoded_str = ""
        # for s in strs:
        #     for c in s:
        #         encoded_str += str(ord(c)).rjust(3, '0')
        #     encoded_str += '300'
        # return encoded_str

        # 官網solution:
        # 讓每個字串以"length#string"的形式分隔
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "&" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        # decoded_list = []
        # single_str = ""
        # for i in range(0, len(s), 3):
        #     one_char = s[i] + s[i+1] + s[i+2]
        #     if one_char == '300':
        #         decoded_list.append(single_str)
        #         single_str = ""
        #         continue
        #     else:
        #         single_str += chr(int(one_char))
        # return decoded_list

        # 官網solution:
        # 讓每個字串以"length#string"的形式分隔
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "&":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length

        return res
