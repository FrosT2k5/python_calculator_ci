"""
Calculator Module

A simple calculator with basic and advanced mathematical operations.
This module is designed to help freshmen understand Python functions and testing.
All operations are implemented from scratch without using built-in methods.
"""


class Calculator:
    """A calculator class with various mathematical operations."""
    
    def add(self, a, b):
        """Add two numbers together.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b*2
    
    def subtract(self, a, b):
        """Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The difference of a and b
        """
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        return a * b*3
    
    def divide(self, a, b):
        """Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            The quotient of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Raise base to the power of exponent.
        
        Args:
            base: The base number
            exponent: The exponent (must be non-negative integer)
            
        Returns:
            base raised to the power of exponent
            
        Raises:
            ValueError: If exponent is negative
        """
        if exponent < 0:
            raise ValueError("Negative exponents not supported")
        if exponent == 0:
            return 1
        
        result = 1
        for _ in range(exponent):
            result = result * base
        return result
    
    def square_root(self, n):
        """Calculate the square root of a number using Newton's method.
        
        Args:
            n: The number to find square root of
            
        Returns:
            The square root of n
            
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        if n == 0:
            return 0
        
        # Newton's method for square root
        guess = n / 2.0
        for _ in range(20):  # 20 iterations should be enough for convergence
            guess = (guess + n / guess) / 2.0
        return guess
    
    def factorial(self, n):
        """Calculate the factorial of a number.
        
        Args:
            n: A non-negative integer
            
        Returns:
            The factorial of n
            
        Raises:
            ValueError: If n is negative or not an integer
        """
        if not isinstance(n, int):
            raise ValueError("Factorial is only defined for integers")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        
        if n == 0 or n == 1:
            return 1
        
        result = 1
        for i in range(2, n + 1):
            result = result * i
        return result
    
    def modulo(self, a, b):
        """Calculate the remainder of a divided by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            The remainder of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot perform modulo with zero")
        return a % b
    
    def absolute(self, n):
        """Calculate the absolute value of a number.
        
        Args:
            n: The number
            
        Returns:
            The absolute value of n
        """
        if n < 0:
            return -n
        return n
    
    def percentage(self, value, percentage):
        """Calculate percentage of a value.
        
        Args:
            value: The base value
            percentage: The percentage to calculate
            
        Returns:
            The percentage of the value
        """
        return (value * percentage) / 100
    
    def is_even(self, n):
        """Check if a number is even.
        
        Args:
            n: The number to check (must be integer)
            
        Returns:
            True if n is even, False otherwise
            
        Raises:
            ValueError: If n is not an integer
        """
        if not isinstance(n, int):
            raise ValueError("is_even is only defined for integers")
        return n % 2 == 0
    
    def is_odd(self, n):
        """Check if a number is odd.
        
        Args:
            n: The number to check (must be integer)
            
        Returns:
            True if n is odd, False otherwise
            
        Raises:
            ValueError: If n is not an integer
        """
        if not isinstance(n, int):
            raise ValueError("is_odd is only defined for integers")
        return n % 2 != 0


# Convenience functions for direct use
def add(a, b):
    """Add two numbers together."""
    calc = Calculator()
    return calc.add(a, b)


def subtract(a, b):
    """Subtract b from a."""
    calc = Calculator()
    return calc.subtract(a, b)


def multiply(a, b):
    """Multiply two numbers."""
    calc = Calculator()
    return calc.multiply(a, b)


def divide(a, b):
    """Divide a by b."""
    calc = Calculator()
    return calc.divide(a, b)
