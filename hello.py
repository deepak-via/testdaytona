def hello_world():
    """Return a greeting message from E2E Test."""
    return 'Hello from E2E Test 1766585237!'


def calculate_fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> calculate_fibonacci(0)
        0
        >>> calculate_fibonacci(1)
        1
        >>> calculate_fibonacci(5)
        5
        >>> calculate_fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Use iterative approach for better performance
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr
