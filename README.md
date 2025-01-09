# Monty Hall Dilemma Simulation

The Monty Hall dilemma is a probability puzzle based on a game show scenario. In the game, a contestant chooses one of three doors. Behind one door is a car (the prize), and behind the other two are goats. After the contestant selects a door, the host, Monty Hall, who knows where the car is, opens one of the remaining doors to reveal a goat. The contestant then has the option to either stick with their initial choice or switch to the other unopened door.

This Python program simulates the Monty Hall problem and tracks the number of wins based on whether the contestant switches their initial guess after one incorrect door is revealed.

## Running the Program

### Requirements
- Python 3.x

### Steps to Run

1. Pull or copy the code into a file (e.g., `monty_hall.py`).
2. Run the script:

```bash
python monty_hall.py
```

### Configuration

- **`k`**: The number of game simulations to run. Adjust this value to change the number of simulations.
  
  ```python
  k = 1000  # Number of game simulations
  ```

- **`changeGuess`**: Whether the contestant switches their guess. Set to `True` to switch, or `False` to keep the initial guess.

  ```python
  changeGuess = True  # Set to False to stick with the initial guess
  ```

### Output

The program outputs the number of wins out of the total simulations:

```bash
won 667 out of 1000
```
