"""
Test cases for the Calculator module.

This file demonstrates how to write test cases using pytest.
Each test function checks if the calculator operations work correctly.
"""

import pytest
from src.calculator import Calculator


class TestBasicOperations:
    """Test basic arithmetic operations."""
    
    def setup_method(self):
        """Set up a Calculator instance before each test."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.add(-10, 5) == -5
    
    def test_add_zero(self):
        """Test adding zero."""
        assert self.calc.add(0, 5) == 5
        assert self.calc.add(5, 0) == 5
        assert self.calc.add(0, 0) == 0
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert self.calc.subtract(10, 5) == 5
        assert self.calc.subtract(20, 8) == 12
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.subtract(5, -3) == 8
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(7, 8) == 56
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(0, 10) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert self.calc.multiply(-3, 4) == -12
        assert self.calc.multiply(-3, -4) == 12
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(20, 4) == 5
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises a ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert self.calc.divide(0, 5) == 0


class TestAdvancedOperations:
    """Test advanced mathematical operations."""
    
    def setup_method(self):
        """Set up a Calculator instance before each test."""
        self.calc = Calculator()
    
    def test_power_positive_exponent(self):
        """Test raising to a positive power."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25
        assert self.calc.power(10, 0) == 1
    
    def test_power_negative_base(self):
        """Test raising negative base to a power."""
        assert self.calc.power(-2, 2) == 4
        assert self.calc.power(-2, 3) == -8
    
    def test_power_negative_exponent_raises_error(self):
        """Test that negative exponents raise a ValueError."""
        with pytest.raises(ValueError, match="Negative exponents not supported"):
            self.calc.power(2, -1)
    
    def test_square_root_positive_numbers(self):
        """Test square root of positive numbers."""
        assert abs(self.calc.square_root(4) - 2.0) < 0.0001
        assert abs(self.calc.square_root(9) - 3.0) < 0.0001
        assert abs(self.calc.square_root(16) - 4.0) < 0.0001
    
    def test_square_root_zero(self):
        """Test square root of zero."""
        assert self.calc.square_root(0) == 0
    
    def test_square_root_negative_raises_error(self):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-4)
    
    def test_factorial_positive_numbers(self):
        """Test factorial of positive numbers."""
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(5) == 120
        assert self.calc.factorial(6) == 720
    
    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            self.calc.factorial(-5)
    
    def test_factorial_non_integer_raises_error(self):
        """Test that factorial of non-integer raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is only defined for integers"):
            self.calc.factorial(3.5)
    
    def test_modulo_positive_numbers(self):
        """Test modulo operation with positive numbers."""
        assert self.calc.modulo(10, 3) == 1
        assert self.calc.modulo(20, 7) == 6
        assert self.calc.modulo(15, 5) == 0
    
    def test_modulo_by_zero_raises_error(self):
        """Test that modulo by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot perform modulo with zero"):
            self.calc.modulo(10, 0)
    
    def test_absolute_positive_numbers(self):
        """Test absolute value of positive numbers."""
        assert self.calc.absolute(5) == 5
        assert self.calc.absolute(10) == 10
    
    def test_absolute_negative_numbers(self):
        """Test absolute value of negative numbers."""
        assert self.calc.absolute(-5) == 5
        assert self.calc.absolute(-10) == 10
    
    def test_absolute_zero(self):
        """Test absolute value of zero."""
        assert self.calc.absolute(0) == 0
    
    def test_percentage(self):
        """Test percentage calculation."""
        assert self.calc.percentage(100, 10) == 10
        assert self.calc.percentage(200, 50) == 100
        assert self.calc.percentage(80, 25) == 20
    
    def test_is_even(self):
        """Test checking if numbers are even."""
        assert self.calc.is_even(2) == True
        assert self.calc.is_even(4) == True
        assert self.calc.is_even(0) == True
        assert self.calc.is_even(3) == False
        assert self.calc.is_even(-2) == True
    
    def test_is_even_non_integer_raises_error(self):
        """Test that is_even with non-integer raises ValueError."""
        with pytest.raises(ValueError, match="is_even is only defined for integers"):
            self.calc.is_even(3.5)
    
    def test_is_odd(self):
        """Test checking if numbers are odd."""
        assert self.calc.is_odd(3) == True
        assert self.calc.is_odd(5) == True
        assert self.calc.is_odd(2) == False
        assert self.calc.is_odd(0) == False
        assert self.calc.is_odd(-3) == True
    
    def test_is_odd_non_integer_raises_error(self):
        """Test that is_odd with non-integer raises ValueError."""
        with pytest.raises(ValueError, match="is_odd is only defined for integers"):
            self.calc.is_odd(3.5)


class TestEdgeCases:
    """Test edge cases and special scenarios."""
    
    def setup_method(self):
        """Set up a Calculator instance before each test."""
        self.calc = Calculator()
    
    def test_large_numbers(self):
        """Test operations with large numbers."""
        assert self.calc.add(1000000, 2000000) == 3000000
        assert self.calc.multiply(1000, 1000) == 1000000
    
    def test_floating_point_operations(self):
        """Test operations with floating point numbers."""
        assert abs(self.calc.add(0.1, 0.2) - 0.3) < 0.0001
        assert abs(self.calc.divide(1, 3) - 0.3333) < 0.001
    
    def test_chained_operations(self):
        """Test performing multiple operations in sequence."""
        # (5 + 3) * 2 = 16
        result = self.calc.add(5, 3)
        result = self.calc.multiply(result, 2)
        assert result == 16
        
        # (10 - 4) / 2 = 3
        result = self.calc.subtract(10, 4)
        result = self.calc.divide(result, 2)
        assert result == 3
