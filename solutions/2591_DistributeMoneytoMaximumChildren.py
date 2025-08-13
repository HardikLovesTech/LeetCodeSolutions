class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1  # not enough to give $1 to each child

        extra = money - children
        max_eights = min(extra // 7, children)

        # If all children are at 8, but leftover still exists -> invalid
        if max_eights == children:
            if extra == max_eights * 7:
                return children
            else:
                return children - 1  # can't distribute leftover to anyone else

        # Check if giving remaining child exactly $4 (1 + 3)
        if (extra - max_eights * 7) == 3 and (children - max_eights) == 1:
            return max_eights - 1

        return max_eights
