from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []


        for i in range(numRows):
            row = [1]

            if i > 0:
                prev = triangle[i-1]
                for j in range(1 , i):
                    value = prev[j-1] + prev[j]
                    row.append(value)
                row.append(1)
            triangle.append(row)
        return triangle