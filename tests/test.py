from .base_tests import Base

class Testidentifier(Base):
    def test_zeros(self, setUp):
        #One and all sides zero
        assert setUp.check(0, 0, 0) == False

    def test_limit_sum(self, setUp):
        #One side greater than the sum of all divided by two
        assert setUp.check(10, 10, 100) == False

    def test_limit_equality(self, setUp):
        #One side equal to the sum of the other two
        assert setUp.check(40, 40, 80) == False

    def test_scalene_triangle(self, setUp):
        #scalene triangle, all sizes with diferent values
        assert setUp.check(50, 70, 80) == True

    def test_isosceles_triangle(self, setUp):
        #isoceles triangle, two equal sides
        assert setUp.check(10, 10, 12) == True

    def test_equilateral_triangle(self, setUp):
        #equilateral triangle, all equal sides
        assert setUp.check(30, 30, 30) == True