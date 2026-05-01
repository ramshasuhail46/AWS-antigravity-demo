# AWS Antigravity Demo

A basic FastAPI app to calculate order total including tax.

## Recent Fixes
**Bug:** The `calculate_total` endpoint previously subtracted the tax amount from the total and had floating point precision issues.
**Fix:** The logic was updated to add the tax properly, and `round(..., 2)` was used to ensure proper 2-decimal floating point representation.
