# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The first time I ran the game, it looked very simple. I was expecting to submit a guess number, the game let me know if I won or lose, and then instruct me to submit another guess if I wanted to keep playing.

The first bug I noticed was that the "New Game" button wasn't working. I submitted my first guess and the game told me that I won, then I clicked new game, and nothing worked. The second bug I noticed was the inconsistency between the range of guess numbers.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input     | Expected Behavior | Actual Behavior | Console Output / Error |
|-------    |-------------------|-----------------|------------------------|
| Guess of  | " Go Higher" hint | No hint         | None                   |
| 25 on the |                   |                 |                        |
| Easy level|                   |                 |                        |
|--------------------------------------------------------------------------|
| Guess of  | "Go Higher" hint  | No hint         | None                   |
| 125 on the|                   |                 |                        |
| Normal    |                   |                 |                        |
| level     |                   |                 |                        |
|--------------------------------------------------------------------------|
|Guess of 12| "Go Lower" hint   | "Go Higher" hint| None                   |
|if secret  |                   |                 |                        |
|is 10      |                   |                 |                        |
|--------------------------------------------------------------------------|


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Cluade Code to refactor the code by separating the game logic from the UI code. It helped me move the logic functions from app.py to logic_utils.py, and updated app.py to import them. Its suggested refactored code worked well. I verified them by manually inspecting the code and testing the behavior of the game. The functions were very similar to the ones originally in app.py, and the game behavior did not change after refactoring. For example, when I entered 45 as a guess number, the game would still hint me to "Go Lower" because the secret number was 13. This shows that the check_guess function still works perfectly.   
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Claude Code helped me to generate a pytest file to run tests on the guessing logic. I ran a test on the "Too High" hint. A function was defined to check whether a guess number is higher than the secret number. I input 60 as a guess, while the secret is 50 and ran the test, and it passed. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit is an open-source Python framework that allows you to turn a script into an interactive web application with just a few lines of code. The script reruns from top to bottom on every execution. For example, if you click a button or change a text input on the UI and rerun, the whole file re-executes from line 1, wiping away every input or event happened before the re-execution. Session state solves this. It's a dictionary that survives across reruns. When events or inputs are held in session states they're not wiped out after a rerun. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One strategy from this project that I want to reuse in future labs or projects is the testing strategy of generating a pytest and then manually testing a logic.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time I work with AI on a coding task, I would use better prompting strategies to get the best results.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
During this project, I understood that some AI generated code looks good and works, but it doesn't gaurantee 100% correctness. Just because it works for a certain input or edge case doesn't mean that it works for all inputs or edge cases.