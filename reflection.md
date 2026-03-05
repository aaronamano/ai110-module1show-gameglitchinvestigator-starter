# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. **when i guessed a number lower or higher than the actual target, it did the opposite. for example if the target was 55 and i guessed 44, the program would tell me to go lower, and if the target was 55 and i guessed 60, the program would tell me to go higher. i expected the program to tell me to go lower if my guess was higher than the target or to go higher if my guess was lower than the target**

2. **when i tried to refresh the game by clicking on New Game, my guesses didn't clear. my guesses/attempts were supposed to be cleared and shown as an empty array in the History part of the Developer Debug Info when i clicked on New Game but those attempts in the History array still persisted**

3. **when i locked in my guess and submitted my guess once, it was supposed to decrement the number of attempts and add it to the History array. however, the number of attempts didn't decrement and it wasn't added in the History array when i locked in my guess and submitted my guess. i had to click it again**

4. **when i ran the app on startup, it initially showed n Attempts Allowed but it showed n-1 Attempts Left. Attempts Allowed and Attempts Left should be the same**

5. **i noticed that when i put a negative number or a number over 100, it didn't show an error message. it should show an error message stating that the user needs to enter a number between 1 to 100**

 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
