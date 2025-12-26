# 🧩 Maze Game (Python Turtle)

A 2D maze adventure game built using **Python Turtle graphics**. The player navigates through maze levels, collects treasures, avoids enemies, and progresses to the next level upon completion.

---

## 🎮 Game Features

- 🧱 Grid-based maze system
- 👤 Player movement using arrow keys
- 💰 Collectible treasures (score-based)
- 👾 Intelligent enemies that chase the player
- 🧠 Two difficulty levels (Level 1 & Level 2)
- 🔁 Restart, Exit, and Next Level buttons
- 🏆 Score tracking

---

## 🗂️ Project Structure

```
maze-game/
│
├── main.py                # Main game file
├── levels.py              # Maze layouts (level_1, level_2)
├── sprites.py             # Sprite image list
├── assets/
│   ├── player-right.gif
│   ├── player-left.gif
│   ├── enemy-right.gif
│   ├── enemy-left.gif
│   ├── gold.gif
│   ├── jungle.gif
│   ├── restart.gif
│   ├── exit.gif
│   └── nextlevel.gif
└── README.md
```

---

## ⚙️ Requirements

- Python **3.8+**
- Turtle module (comes pre-installed with Python)

No external libraries are required.

---

## ▶️ How to Run

1. Clone or download the project
2. Make sure all `.gif` sprite files are in the correct folder
3. Run the main file:

```bash
python main.py
```

---

## 🎯 Controls

| Key | Action |
|----|-------|
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |

---

## 🧠 Game Logic Overview

### Player
- Moves in 24x24 grid blocks
- Cannot pass through walls
- Collects treasures to increase score

### Enemies
- Move randomly
- Chase player when within a certain distance
- Collision with enemy ends the game

### Levels
- **Level 1**: 2 enemies
- **Level 2**: 4 enemies (higher difficulty)

### Winning Conditions
- Collect all treasures in a level
- Level 1 → unlocks Level 2
- Level 2 → final victory screen

---

## 🔁 Game States

- **Running** – Normal gameplay
- **Game Over** – Player hit by enemy
- **Level Complete** – All treasures collected

Buttons appear accordingly:
- 🔄 Restart
- ❌ Exit
- ⏭️ Next Level

---

## 🚀 Future Improvements

- Add BFS / DFS / A* auto-solving
- Add sound effects & background music
- Add score leaderboard
- Add more levels
- Add enemy pathfinding

---

## 👩‍💻 Author

**Noorbano Shaikh**  
BS Computer Science (Final Year)

---

## 📜 License

This project is for **educational purposes**. You are free to modify and enhance it.

---

✨ Enjoy the game and happy coding!

