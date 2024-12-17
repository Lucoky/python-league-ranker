# League Ranking CLI (Python)

A command-line application to calculate and display the ranking table for a league based on match results. Built with Python.

---

## Table of Contents
1. [Overview](#overview)
2. [Rules](#rules)
3. [Sample Input/Output](#sample-inputoutput)
4. [How to Run](#how-to-run)
5. [Tests](#tests)

---

## Overview

This application reads match results, calculates points for each team, and displays a ranked leaderboard. The ranking follows the rules outlined below, and the output is sorted by points and team names.

---

## Rules

1. **Points system:**
   - A win = **3 points**
   - A draw = **1 point**
   - A loss = **0 points**

2. **Tie-breaking:**
   - Teams with the same points share the same rank.
   - Teams are sorted alphabetically if their points are tied.

3. **Input/Output:**
   - Input consists of results of matches (text file or stdin).
   - Output is a sorted ranking table.

---

## Sample Input/Output

### Input
```
Lions 3, Snakes 3
Tigers 1, Lions 2
Snakes 0, Tigers 1
Lions 1, Snakes 0
Tigers 3, Lions 3
```

### Output
```
1. Lions, 8 pts
2. Tigers, 7 pts
3. Snakes, 1 pt
```

---

## How to Run

### Prerequisites
- Python 3.7 or higher installed on your machine.

### Steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/lucoky/python-league-ranker.git
   cd python-league-ranker
   ```

2. Run the application:
    - Using a text file input:
      ```bash
      python app.py sample_input.txt
      ```
    - Using standard input:
      ```bash
      python app.py
      ```

---

## Tests

To run automated tests:
```bash
python -m unittest test_app.py
```

---

## Dependencies

- No external libraries are required.
