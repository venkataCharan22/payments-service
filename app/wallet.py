"""Wallet operations — BUG: no None check on user lookup."""

USERS = {
    1: {"id": 1, "balance": 250.00, "currency": "USD"},
    2: {"id": 2, "balance": 1300.50, "currency": "EUR"},
}


def get_balance(user_id):
    """Return the user's current balance."""
    user = USERS.get(user_id)
    # BUG: blows up with AttributeError for unknown user
    return f"{user['balance']:.2f} {user['currency']}"


def credit(user_id, amount):
    user = USERS.get(user_id)
    if user is None:
        return None
    user["balance"] += amount
    return user["balance"]
