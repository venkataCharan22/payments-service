# payments-service

A small payment-processing microservice with intentional bugs for Bug2PR demos.

## Bugs in this repo

- `app/wallet.py` — Wallet.get_balance crashes on missing user
- `app/charges.py` — Divide by zero when computing average transaction
- `app/refunds.py` — KeyError when refund metadata is missing
