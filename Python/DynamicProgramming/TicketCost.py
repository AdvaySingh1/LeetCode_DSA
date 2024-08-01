from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # tabular (bottom up)
        cache = {} # day
        for i in range(len(days)):
            cache[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                daysBefore = i
                while daysBefore >= 0 and days[daysBefore] > days[i] - d:
                    daysBefore -= 1
                cache[i] = min(cache[i], c + cache.get(daysBefore, 0)) 

        return cache[len(days) - 1] # the last real day cache




        # memoization solution O(n * m)
        cache = {} # day
        def memoization(day):
            if day == len(days):
                return 0
                
            if day in cache:
                return cache[day]

            cache[day] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                nextDay = day

                # do to the next possible day
                # this doen't add anything but a constant to the time complexity
                while nextDay < len(days) and days[nextDay] < days[day] + d: # 
                    nextDay += 1
                cache[day] = min(cache[day], c + memoization(nextDay))
            return cache[day]
        
        return memoization(0)

        # brute force solution
        # O(n^m)
        days = set(days)
        finalDay = max(days)
        def bruteForce(day):
            if day > finalDay:
                return 0
            while day not in days:
                day += 1
            # which to include
            oneDayCost = bruteForce(day + 1) + costs[0]
            sevenDayCost = bruteForce(day + 7) + costs[1]
            thirtyDayCost = bruteForce(day + 30) + costs[2]
            return min(oneDayCost, sevenDayCost, thirtyDayCost)
        
        return bruteForce(0)
