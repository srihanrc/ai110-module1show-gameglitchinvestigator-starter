# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

It showed the developer debug info which shows the amount of given attempts and that the user needed to guess a number between 1 and 100. It also shows the actual secret guess.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The hints were messed up as when the secret number was higher than the users guess the hint would say go lower instead of go higher and the same is vice versa. What should happen is if my guess is lower than the secret number, the hint should tell me go higher and vice versa. Also another bug that I found is when I submit the right guess it tells me to click new game to play again but when I click it the button doesn't function and I can't play a new game. What should happen is when I click the new game button, I should be able to enter my guess and play again.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
   12       Go Higher!           Go Lower!        Opposite Behavior
|  22   |   Go Lower!       |    Go Higher!   |   Opposite Behavior    |
|Incorrect Guess| Score = 0  |   Score = -5   | Score goes to negative value for each incorrect guess.|
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Github Copilot for this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The AI suggestion was correct on the changes it made for the bug on hints where it switched the go higher with go lower and vice versa.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I noticed that the attempts wouldn't go down from 8 to 7 the first time when I guessed an incorrect number. I told AI to fix the bug in app.py to make the attempts go down but it made changes in test_game_logic.py as well which I knew didn't make sense.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I would rerun my program and test the game based on that bug to see if it works the way it should.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One test I ran using pytest was the test guess too low and test guess too high. This showed some changes for the code and gave me the option to keep or undo the changes. It then told me to run the cmd.EXE command within the gameglitch-investigator folder.

- Did AI help you design or understand any tests? How?

The AI helped me to design tests since this gave good function names which helped me understand what the test case was for and it showed the changes it made from the previous code to current. AI however didn't help me understand any tests since it just showed me the changes but never explained why the changes were being made.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

When running Streamlit when you click a button this would rerun the code and show a new display. Everything basically resets.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

I definitely would tell copilot to fix any bugs and write test cases for my projects as before I relied on copy paste into claude or perplexity to find errors in code.

- What is one thing you would do differently next time you work with AI on a coding task?

I will tell the AI to explain why it gave me the edited code and what the code is intended to do so that way I know whether the AI change makes sense or not since for this assignment it just gave me changes without really explaining what the change is doing.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I think AI generated code is beneficial to fix any bugs you have with the project as this is much easier than manually having to search your code for any errors. However I would not use AI generated code for the project itself since the AI wouldn't fully be able to develop code that fits the standard.