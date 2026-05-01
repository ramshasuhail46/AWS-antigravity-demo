---
name: qa-pro
description: Autonomous QA agent that fixes code on a new branch and requests a human review.
---

# QA & Review Mission

## Phase 1: Isolation
1. **Create Branch**: Create a new branch named `fix/logic-error` using the terminal.
2. **Switch**: Ensure you are working on this new branch before making any edits.

## Phase 2: Fix & Validate
1. **Test**: Write a `pytest` file in `/tests` to catch the bug in `main.py`.
2. **Repair**: Edit `main.py` to fix the calculation logic.
3. **Verify**: Run the tests again. Do not proceed until the terminal shows a "Passed" status.

## Phase 3: The Review Request
1. **Commit**: Commit the changes with a clear message: "Fix: Corrected tax calculation logic".
2. **Push**: Push the branch to the remote repository.
3. **PR & Review**: Open the **Browser**. Navigate to GitHub to create a Pull Request. **Crucial**: Use the "Reviewers" sidebar in the GitHub UI to add the repository owner as a reviewer.
4. **Final Artifact**: Post a screenshot of the "Review Requested" status in the chat for confirmation.