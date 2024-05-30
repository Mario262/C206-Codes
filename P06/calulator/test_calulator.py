from calulator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 30
        b = 20
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 50
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 30
        b = 10
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 20
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 20
        b = 3
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 60
        assert result == expected

    def test_divide(self):
        # arrange
        a = 40
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 20
        assert result == expected