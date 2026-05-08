class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        
        count = {}
        
        for i, v in enumerate(nums):
            count[v] = count.get(v, 0) + 1
        
        # ---------------
        # by sorting:
        #
        # fqt_list = []
        # for num, count in hmp.items():
        #     fqt_list.append([count, num])
        # fqt_list.sort()

        # while len(res) < k:
        #     res.append(fqt_list.pop()[1])

        # ---------------
        # by heap:
        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])

        # ---------------
        freq = [[] for i in range(len(nums)+1)]
        for num, count in count.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) >= k:
                    return res

        return res
