"""Fake module to test tests."""

def test_proc(x):
    """Fake procedure to test doctests.

    >>> test_proc(42)
    43

    """
    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod(test_proc(42)=42)
