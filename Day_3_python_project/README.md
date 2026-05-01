# 🔐 TRIPLE - X - PRISON

A terminal-based Python puzzle game where you must crack numeric locks and escape from a high-security prison.

---

## 🎮 Game Overview

You are trapped inside a prison with multiple locked doors.  
Each door is protected by a secret 3-number password.

To unlock each level, you are given:
- ➕ Sum of 3 numbers  
- ✖️ Product of 3 numbers  

Your task is to guess the correct numbers and escape the prison!

---

## 🧠 How to Play

1. The game generates 3 random numbers internally.
2. It displays:
   - Sum of numbers
   - Product of numbers
3. You must guess the correct 3 numbers.
4. Each correct answer unlocks the next level.
5. Wrong answers reduce attempts.

---

## 🏆 Game Features

- 🎲 Random password generation
- 🔐 Multi-level system (5 levels)
- 💀 Attempt-based failure system
- 🎉 Win & Game Over screens
- 🎨 ASCII prison design UI
- ⚡ Terminal-based gameplay

---

## 🛠️ Built With

- Python 3
- random module
- pyfiglet (ASCII text styling)
- colorama (colored terminal output)

---

## 📦 Installation

Install required dependencies:

```bash
pip install pyfiglet colorama
