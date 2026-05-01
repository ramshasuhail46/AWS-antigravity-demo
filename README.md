# AWS Antigravity Demo

## Bug Fix: Order Calculation Float Precision

The `calculate_total` function in `main.py` was returning floating-point results with high precision errors (e.g., `10.840200000000001` instead of `10.84`). To prevent monetary calculation discrepancies, the `total` is now explicitly rounded to two decimal places.

Files changed:
- `main.py`: Fixed the order calculation bug by applying the `round()` built-in function rounding the sum to 2 decimal places.
- `tests/test_main.py`: Created an initial test suite using Pytest and FastAPI's `TestClient` to ensure basic correct functionality and prevent floating point regressions.
