#!/usr/bin/env python3
"""
A simple calculator module with basic arithmetic operations.
"""


class Calculator:
    """A calculator class that performs basic arithmetic operations."""

    def add(self, a, b):
        """
        Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract b from a.

        Args:
            a: First number
            b: Number to subtract

        Returns:
            The difference of a and b
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b
        """
        return a * b

    def divide(self, a, b):
        """
        Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            The quotient of a and b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def main():
    """CLI interface for the calculator."""
    calc = Calculator()

    print("=" * 50)
    print("Simple Calculator")
    print("=" * 50)
    print("\nAvailable operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=" * 50)

    while True:
        try:
            choice = input("\nSelect operation (1-5): ").strip()

            if choice == "5":
                print("Thank you for using the calculator. Goodbye!")
                break

            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice. Please select 1-5.")
                continue

            # Get numbers from user
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            # Perform calculation
            result = None
            operation = ""

            if choice == "1":
                result = calc.add(num1, num2)
                operation = "+"
            elif choice == "2":
                result = calc.subtract(num1, num2)
                operation = "-"
            elif choice == "3":
                result = calc.multiply(num1, num2)
                operation = "*"
            elif choice == "4":
                try:
                    result = calc.divide(num1, num2)
                    operation = "/"
                except ValueError as e:
                    print(f"Error: {e}")
                    continue

            print(f"\nResult: {num1} {operation} {num2} = {result}")

        except KeyboardInterrupt:
            print("\n\nThank you for using the calculator. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
