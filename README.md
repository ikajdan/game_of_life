# Game of Life

A Python object-oriented implementation of Conway's Game of Life, using Pygame for graphical visualization. This application allows for interactive cell placement, random grid generation, and observing the evolution of the cellular automaton.

Conway's Game of Life is a zero-player game where the evolution of a grid of cells is determined by simple rules. It is a classic example of cellular automata and demonstrates how complex patterns can emerge from simple rules.

<br>
<div align="center">
  <img src="https://github.com/user-attachments/assets/fb0dd813-d26b-4aad-b8cd-a62cff96e92f" width="500" height="auto"/>
  <br><br>
  <em>Demo of the game.</em>
</div>
<br>

## Controls

| Key                          | Action                                         |
|------------------------------|------------------------------------------------|
| <kbd>Left Mouse Button</kbd> | Toggle the state of the cell under the cursor. |
| <kbd>Spacebar</kbd>          | Pause/Resume the simulation.                   |
| <kbd>R</kbd>                 | Randomly generate 200 live cells.              |
| <kbd>C</kbd>                 | Clear all cells.                               |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ikajdan/game_of_life
   cd game_of_life
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application with the following command:
```bash
python main.py
```

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for more information.
