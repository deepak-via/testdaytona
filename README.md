# Python Calculator

A simple yet robust command-line calculator application built with Python, featuring basic arithmetic operations and comprehensive error handling.

## Features

- **Basic Arithmetic Operations**
  - Addition
  - Subtraction
  - Multiplication
  - Division with zero-division protection

- **Interactive CLI Interface**
  - User-friendly menu system
  - Input validation
  - Clear error messages

- **Robust Error Handling**
  - Division by zero protection
  - Invalid input handling
  - Graceful exit options

- **Comprehensive Test Coverage**
  - Unit tests for all operations
  - Edge case testing
  - Type handling validation

## Installation

1. Clone the repository or download the files
2. Ensure you have Python 3.6 or higher installed

```bash
python --version
```

## Usage

### Command Line Interface

Run the calculator in interactive mode:

```bash
python calculator.py
```

Follow the on-screen prompts to:
1. Select an operation (1-5)
2. Enter the first number
3. Enter the second number
4. View the result

### Example Session

```
==================================================
Simple Calculator
==================================================

Available operations:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
==================================================

Select operation (1-5): 1
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0

Select operation (1-5): 4
Enter first number: 20
Enter second number: 0
Error: Cannot divide by zero

Select operation (1-5): 5
Thank you for using the calculator. Goodbye!
```

### Using as a Module

You can also import and use the Calculator class in your own Python code:

```python
from calculator import Calculator

calc = Calculator()

# Addition
result = calc.add(10, 5)
print(result)  # Output: 15

# Subtraction
result = calc.subtract(10, 5)
print(result)  # Output: 5

# Multiplication
result = calc.multiply(10, 5)
print(result)  # Output: 50

# Division
result = calc.divide(10, 5)
print(result)  # Output: 2.0

# Division by zero handling
try:
    result = calc.divide(10, 0)
except ValueError as e:
    print(e)  # Output: Cannot divide by zero
```

## Running Tests

Run the unit tests to verify the calculator functionality:

```bash
python test_calculator.py
```

Or run with verbose output:

```bash
python test_calculator.py -v
```

Or use unittest discovery:

```bash
python -m unittest discover
```

### Test Coverage

The test suite includes:
- Basic operation tests for all four arithmetic operations
- Positive and negative number handling
- Floating-point number operations
- Zero handling (addition, subtraction, multiplication)
- Division by zero error handling
- Edge cases (large numbers, very small numbers)
- Mixed type operations (int and float)

## Project Structure

```
.
├── calculator.py       # Main calculator module with Calculator class and CLI
├── test_calculator.py  # Comprehensive unit tests
└── README.md          # This file
```

## API Reference

### Calculator Class

#### Methods

**`add(a, b)`**
- Adds two numbers
- Parameters: `a`, `b` (int or float)
- Returns: Sum of a and b

**`subtract(a, b)`**
- Subtracts b from a
- Parameters: `a`, `b` (int or float)
- Returns: Difference of a and b

**`multiply(a, b)`**
- Multiplies two numbers
- Parameters: `a`, `b` (int or float)
- Returns: Product of a and b

**`divide(a, b)`**
- Divides a by b
- Parameters: `a`, `b` (int or float)
- Returns: Quotient of a and b
- Raises: `ValueError` if b is zero

## Error Handling

The calculator handles various error conditions:

1. **Division by Zero**: Raises a `ValueError` with message "Cannot divide by zero"
2. **Invalid Input**: Prompts user to enter valid numbers
3. **Invalid Menu Choice**: Prompts user to select valid operation (1-5)
4. **Keyboard Interrupt**: Gracefully exits the program

## Best Practices Implemented

- Clear docstrings for all classes and methods
- Type-agnostic operations (works with int and float)
- Comprehensive error handling
- PEP 8 compliant code formatting
- Modular design (class-based implementation)
- Separation of concerns (Calculator class vs CLI interface)
- Extensive unit test coverage
- User-friendly CLI with clear prompts and feedback

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## License

This project is provided as-is for educational purposes.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
