#!/usr/bin/env python3
"""
Example usage of the calculate_fibonacci function.
"""

from hello import calculate_fibonacci


def main():
    """Demonstrate the calculate_fibonacci function with various inputs."""
    print("Fibonacci Sequence Examples:\n")

    # Calculate and display first 15 Fibonacci numbers
    print("First 15 Fibonacci numbers:")
    for i in range(15):
        fib = calculate_fibonacci(i)
        print(f"F({i}) = {fib}")

    print("\n" + "=" * 40 + "\n")

    # Demonstrate specific examples
    examples = [0, 1, 5, 10, 20]
    print("Specific examples:")
    for n in examples:
        result = calculate_fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")

    print("\n" + "=" * 40 + "\n")

    # Demonstrate error handling
    print("Error handling example:")
    try:
        calculate_fibonacci(-5)
    except ValueError as e:
        print(f"Error when n=-5: {e}")


if __name__ == "__main__":
    main()
