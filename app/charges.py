"""Charge & transaction math — BUG: divide-by-zero on empty list."""


def total_charges(charges):
    return sum(c.get("amount", 0) for c in charges)


def average_charge(charges):
    """Compute the average transaction amount."""
    total = total_charges(charges)
    # BUG: divides by zero when charges is empty
    return total / len(charges)


def apply_fee(amount, rate=0.029):
    return round(amount * (1 + rate), 2)
