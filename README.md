# Python Calculator

A simple calculator I built while learning Python, with a small web version on top so it's easier for people to try out in a browser.

## What it does

- Basic operations: addition, subtraction, multiplication, division
- Keeps asking for another calculation until you choose to stop
- Catches division by zero instead of crashing
- Runs two ways: in the terminal (`calculator.py`) or in a browser (`index.html`)

## How it's put together

**`calculator.py`** is the actual calculator — a loop that asks for two numbers and an operator, then prints the result. This is the part I wrote and tested myself while working through Python basics: input handling, conditionals, and loops.

**`index.html`** is a browser version of the same logic. I don't know HTML, CSS, or JavaScript yet, so I used AI to help turn the Python version into something people can click through in a browser instead of typing into a terminal. The math it does is exactly what `calculator.py` does — same operations, same messages — it's just wearing a different interface.

**`vercel.json`** and **`requirements.txt`** were added while I was figuring out how to deploy this. I'm still learning how Vercel handles a Python script versus a static site, so those two files may need some cleanup as I get further along (see the note at the bottom).

## Running it

**Terminal version:**
```bash
python calculator.py
```
Follow the prompts, and type `stop` when you're done.

**Browser version:**
Open `index.html` directly in a browser, or visit the deployed link if it's live.

## Why I made this

This was my first real project after learning Python loops, conditionals, and user input. The browser version came afterward, mostly to see how far I could push something I'd already built by hand — even into territory (HTML/CSS/JS) I haven't learned yet.

## Known rough edge

`requirements.txt` lists Flask, but `calculator.py` is a plain terminal script with no Flask app in it, and `index.html` does all its math in the browser rather than calling a backend. So right now the Flask dependency and the `api/*.py` route in `vercel.json` aren't actually used by anything. It's on my list to either build out a real API version or simplify the config to match what's actually deployed.

---

Feedback is welcome — I'm still learning.