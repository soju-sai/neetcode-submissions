from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # edge cases: str是[""]、一個item
        # 迴圈每個strs的item
        # 確認：
        # 1. dic中，tuple key是否存在
        # 2. tuple key存在，tuple[k].append(item)
        # 3. tuple key不存在，d[tuple key]
        dic1 = defaultdict(list)
        if len(strs) == 1:
            return [strs]
        else:
            for i in strs:
                tk = self.getTupleKey(i)
                dic1[tk].append(i)
            return list(dic1.values())
    
    def getTupleKey(self, str_input):
        dic2 = {}
        for s in str_input:
            dic2[s] = dic2.get(s, 0) + 1
        # Sort items to ensure consistent tuple key for same character frequencies
        return tuple(sorted(dic2.items()))