# AWS Antigravity Demo

This project provides a simple FastAPI endpoint to calculate the total price of an order including tax.

## Features
- **FastAPI**: Modern, fast (high-performance) web framework.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Decimal Precision**: Uses the `Decimal` class for accurate financial calculations, avoiding common floating-point errors.
- **Rounding**: Results are rounded to 2 decimal places using `ROUND_HALF_UP`.

## Fixed Bug
- **Issue**: The original implementation used `float` for `amount` and `tax_rate`, which caused precision errors in financial calculations (e.g., `105.10499999999999` instead of `105.105`).
- **Fix**: Switched to `decimal.Decimal` for all calculations and implemented explicit rounding to 2 decimal places.

## Setup
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests
```bash
export PYTHONPATH=$PYTHONPATH:.
pytest tests/test_main.py
```
