class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter

        freq = Counter(word)

        for ch in freq:
            freq[ch] -= 1

            # Remove the character from dict if its count becomes 0
            temp = {k: v for k, v in freq.items() if v > 0}
            values = list(temp.values())

            # Check if all remaining frequencies are equal
            if len(set(values)) == 1:
                return True

            freq[ch] += 1  # Restore for next iteration

        return False
