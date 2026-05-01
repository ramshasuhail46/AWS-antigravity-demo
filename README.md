# AWS Antigravity Demo

## Bug Fixes
- **Agent Fix**: Fixed a bug in `main.py` where floating point arithmetic could lead to precision errors when calculating order totals. The `calculate_total` function now correctly rounds the total order amount to 2 decimal places. A Pytest suite was also added to ensure calculation logic remains sound.
