"""Refund processing — BUG: assumes 'metadata' key exists."""


def process_refund(refund):
    """Process a single refund."""
    # BUG: KeyError when refund has no 'metadata' field
    reason = refund["metadata"]["reason"]
    return {"status": "refunded", "reason": reason, "amount": refund["amount"]}
