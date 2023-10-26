class Triangle:

    def check(self, side_a, side_b, side_c): 
        if side_a == 0 or side_b == 0 or side_c == 0:
            return False

        limit = (side_a + side_b + side_c) / 2
        if side_a >= limit or side_b > limit or side_c >= limit:
            return False

        if side_a == side_b + side_c or side_b == side_a + side_c or side_c == side_a + side_b:
            return False
        
        return True