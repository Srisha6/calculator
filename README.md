# 🧮 Tkinter Calculator

This is my first GUI project, built while learning Python's Tkinter library. 
It started as a basic calculator and grew into something with a dark theme, 
keyboard support, and a few scientific functions like square root and square.

## What it can do
- Handles all basic operations — addition, subtraction, multiplication, division
- Square root (√) and square (x²) at the click of a button
- Percentage conversion
- Type directly from your keyboard — no need to click every button
- Press Enter to calculate, Backspace to delete

## Why I built this
I'm a B.Tech AI & Data Science student exploring GUI development as part of 
my journey into Python. This project helped me understand how buttons, 
layouts, and event handling work together in a real application.

## Tech Used
- Python 3
- Tkinter (no extra installation needed)

## Run it yourself
```bash
python calculator.py
```

## Behind the scenes
- Used `grid()` to arrange buttons in a clean layout
- `eval()` handles the actual math
- `try/except` so the app doesn't crash on invalid input
- Color-coded buttons (orange = operators, yellow= scientific functions, 
  green = equals, red = clear)

## What's next
Planning to add memory functions and a history of past calculations.

---
*Built by Srisha
