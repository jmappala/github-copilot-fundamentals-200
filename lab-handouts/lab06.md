# Documentation Actions with GitHub Copilot

## Generating Docstrings with GitHub Copilot 
1. Open `game-python.py` in your editor

2. Open inline GitHub Copilot Chat by pressing **ctrl + I**

3. Prompt Copilot Chat with the following prompt: 

```
Create docstrings for the functions in this file
```

4. Iterate through suggestions and accept as needed

## Generating Documentation with GitHub Copilot

5. Open the `game-documentation.md` file from the `lab-files` directory

6. Open GitHub Copilot Chat and prompt it to generate documentation for the files in the `lab-files` directory. Do this by breaking the prompt into tasks:

- `Generate markdown documentation for game.java it should explain what the code does and how to run it`

6a. Add the result into `game-documentation.md` 

- `Generate markdown documentation for gameComparison.java it should explain what the code does and how to run it`

6b. Add the result into `game-documentation.md` 

- `Generate markdown documentation for game-python.py it should explain what the code does and how to run it`

6c. Add the result into `game-documentation.md` 

- `Generate markdown documentation for the test suite in the lab-files directory`

6d. Add the result into `game-documentation.md`

# Doc to Code with GitHub Copilot 

7. Open the `extra-documentation.md` file in your window

8. Prompt GitHub Copilot to generate a C# file from the documentation in `extra-documentation.md`

```
Using extra-documentation.md create a C# file for a rock-paper-scissors program
```

9. Add the results into `game.cs`