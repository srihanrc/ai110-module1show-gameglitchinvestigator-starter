# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.

The goal of this game is to find the secret number in a certain amount of attempts. There is optional hint that tells whether to go higher or lower.

- [ ] Detail which bugs you found.

Some bugs I found were that one the go higher and go lower hints were doing opposite tasks. When the user had to actually go lower to get the secret number it instead said go higher and vice versa. Another bug that I found was that the user can't click new game either during the round or after the game was finished.

- [ ] Explain what fixes you applied.

I used github copilot and I noticed that the bug was occurring in app.py. So I used the # FIXME: and told copilot to make changes to the go higher and go lower functions as they were doing the opposite tasks. I also told copilot that the new game button was bugged and nothing happened and to write code for the button.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. You have a limited amount of attempts. Type in a guess that you think is the secret number.
2. Based on the number it will either tell you that you got the number or you didn't.
3. You have the option to use a hint which tells you to go higher or go lower.
4. Following the hint makes it easier to guess the secret number.
5. If the user guesses the secret number they will earn points.
6. If they don't guess the number they won't earn any points.
7. The user can start a new game whenever they want. 


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```                                                                                                       

test_game_logic.py ......                                                                                            [100%]

==================================================== 6 passed in 0.06s ====================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
