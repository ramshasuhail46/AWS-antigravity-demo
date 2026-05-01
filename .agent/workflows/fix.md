---
description: Automatically detects bugs in the current branch, creates a fix branch, runs tests, and prepares a GitHub PR with a review request.
---

The user wants to transition from "Implementation" to "Verification" without manual intervention.

# Execution Steps
1. **Branching**: Immediately create a new branch named `agent-fix-{{timestamp}}`.
2. **Analysis**: Scan `main.py` for logical or syntax errors.
3. **Testing**: 
    - Create a `tests/` directory if it doesn't exist.
    - Write a `pytest` file that asserts the correct logic for the calculation.
    - Run `pytest` in the terminal.
4. **Self-Correction**: If the terminal output shows a failure, the agent must rewrite the buggy lines in `main.py` and re-run the tests until they pass.
5. **Documentation**: Update the `README.md` to reflect that a bug was found and fixed by the agent.
6. **PR & Review**:
    - Push the branch to GitHub.
    - Open the Chrome browser.
    - Create a Pull Request and set the repository owner as the 'Required Reviewer'.