import pytest
from src.triangle import Triangle

class Base:

    @pytest.fixture
    def setUp(self):
        triangle = Triangle()
        return triangle