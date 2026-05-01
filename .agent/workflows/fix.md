---
description: Automatically detects bugs in the current branch, creates a fix branch, runs tests, and prepares a GitHub PR with a review request.
---

# Intent
The user wants to transition from "Implementation" to "Verification" without manual intervention.

# Execution Steps
1. **Branching**: Immediately create a new branch named `agent-fix-{{timestamp}}`.
2. **Analysis**: Scan `main.py` for logical or syntax errors.
3. **Testing**: 
    - Create a `tests/` directory if it doesn't exist.
    - Write a `pytest` file that asserts the correct logic for the calculation.
    - Run `pytest` in the terminal.
4. **Self-Correction**: If the terminal output shows a failure, the agent must rewrite the buggy lines in `main.py` and re-run the tests until they pass.
5. **Documentation**: Update the `README.md` to reflect the specific bug found and the fix applied.
6. **PR & Review**:
    - **Push**: Push the current branch to the remote origin.
    - **Navigate**: Open the Chrome browser and go to the GitHub "New Pull Request" page for this repo.
    - **Wait**: Explicitly wait for the page to fully load.
    - **Draft**: Use the browser tool to type a detailed summary of the fix in the 'Description' box.
    - **Reviewer**: Search for the repository owner (the user) in the 'Reviewers' sidebar and select them.
    - **Submit**: Autonomously click the green 'Create pull request' button.
    - **Confirmation**: Take a screenshot of the completed PR page and post it as an artifact.