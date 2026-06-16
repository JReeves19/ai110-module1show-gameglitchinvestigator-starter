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

- The game generates a secret number and allow users to guess that number. It return hints like "Go HIGHER" or "Too Low" if the guess is less than the secret number, and "Go LOWER" or "Too High" if the guess if greater than the secret number.
- When I first tried the game, I found that the hints were misleading. For example, when the secret number was 24 and I entered 16 as a guess, the game returned "Go LOWER".
- There was a logic break in the if statement initially on lines 43-48 in app.py. The program was returning "Too High" or "Go HIGHER" if the guess was greater than the secret. I swapped the "Go HIGHER" hint to "Go LOWER".  

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 56
2. The game returns "Go HIGHER"
3. User enters a guess of 89. The game returns "Go LOWER".
4. The game correctly updates the user score after each guess.
5. The game ends after user correctly guess the secret number.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

pytest tests/test_game_logic.py -v
=============== test session starts =========================================
platform win32 -- Python 3.13.14, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\jaket\CodePath\Week-2\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jaket\CodePath\Week-2\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 7 items                                                                                                                                                                                                                              

tests/test_game_logic.py::test_winning_guess PASSED                                                                                                                                                                                      [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                                                                                                                     [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                                                                                                                      [ 42%]
tests/test_game_logic.py::test_hint_says_go_lower_when_guess_too_high PASSED                                                                                                                                                             [ 57%]
tests/test_game_logic.py::test_hint_says_go_higher_when_guess_too_low PASSED                                                                                                                                                             [ 71%]
tests/test_game_logic.py::test_hint_correct_with_string_secret_too_high PASSED                                                                                                                                                           [ 85%]
tests/test_game_logic.py::test_hint_correct_with_string_secret_too_low PASSED                                                                                                                                                            [100%]
$====================== 7 passed in 0.05s ======================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
