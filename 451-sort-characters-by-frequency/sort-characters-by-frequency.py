class Solution:
    def frequencySort(self, words: str) -> str:
        def getFreq(s):
            freq = {}
            for letter in s:
                if letter in freq:
                    freq[letter] += 1
                else:
                    freq[letter] = 1
            return freq

        freq = getFreq(words)

        sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        result = ''.join([char * count for char, count in sorted_chars])

        return result
