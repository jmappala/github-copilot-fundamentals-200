# Creating Unit Tests with GitHub Copilot Chat

1. Ensure that all of your files that have been created so far are open in your VS Code window: 

- `game.java`
- `gameComparison.java`
- `gameRefactored.java`
- `game-python.py`

2. Open the GitHub Copilot Chat window to ask a few questions about testing (ask 1 question, then the next)

- What is the naming convention for test suites in Python?

2a. Following the feedback from GitHub Copilot Chat, create a `tests` directory in the `lab-files` directory. Create a file named `test_game.py`

- How can I run tests in my terminal?

2b. Take note of the command for future use

- What is testing code coverage?

2c. Take note of the answer for future use

3. Create test cases for `game-python.py` using the prompt below

```
/tests create a test suite for game-pyton.py
```

4. Insert the suggested tests into `test_game.py` and run using the command found in step 2b