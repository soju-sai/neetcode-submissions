class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights) # point
        res = r

        while l <= r:
            capacity = (l + r) // 2
            runDays = 1 # point
            loadWeight = capacity
            for w in weights:
                if loadWeight - w < 0:  # point
                    runDays += 1
                    loadWeight = capacity
                loadWeight -= w
                if runDays > days:
                    break

            if runDays <= days:
                res = min(capacity, res)
                r = capacity - 1
            else:
                l = capacity + 1

        return res

    def shipWithinDays_v1(self, weights: List[int], days: int) -> int:
        l, r = 1, max(weights)
        res = r

        while l <= r:
            capacity = (l + r) // 2
            runDays = 0
            loadWeight = capacity
            for w in weights:
                loadWeight -= w
                if loadWeight <= 0:
                    loadWeight = capacity + loadWeight
                    runDays += 1
                if runDays > days:
                    break
            print(capacity, runDays)

            if runDays <= days:
                res = capacity
                r = capacity - 1
            else:
                l = capacity + 1

        return res