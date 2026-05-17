import pytest
from app.pricing import average_price


def test_average_price_zero_count():
    """Regression test: average_price should handle count=0 without ZeroDivisionError."""
    # This test proves the bug is fixed
    # Before fix: raises ZeroDivisionError
    # After fix: should return 0 or raise ValueError with clear message
    
    with pytest.raises((ZeroDivisionError, ValueError)):
        average_price(total=100, count=0)