# AWS Antigravity Demo

This project provides a FastAPI endpoint to calculate the total price of an order including tax.

## Fixed Bug
- **Bug**: The calculation logic was subtracting tax from the amount instead of adding it.
- **Fix**: Updated the formula in `main.py` to correctly add the tax rate percentage to the base amount.

## Testing
To run tests:
```bash
python3 -m pytest tests/test_main.py
```
