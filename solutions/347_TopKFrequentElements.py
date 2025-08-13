from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Find the maximum frequency
        maxFreq = max(freq.values())

        # Create buckets based on frequencies
        # Each bucket index represents frequency
        buckets = [[] for _ in range(maxFreq + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Collect top k frequent elements
        res = []
        for i in range(maxFreq, 0, -1):
            buckets[i].sort(reverse=True)

            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res