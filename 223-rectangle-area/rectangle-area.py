class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        int_area = (max((min(ay2, by2)-max(ay1, by1)),0)*               #  int_area is the area of the rectangles' 
                    max((min(ax2, bx2)-max(ax1, bx1)),0))               #  intersection. If no intersection, int_area == 0
                       
        return ((ax2-ax1)*(ay2-ay1) +                                   #  area of rectangle A +
                (bx2-bx1)*(by2-by1) -                                   #  area of rectangle B -
                int_area              )                                 