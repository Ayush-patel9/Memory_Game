# Planetary Pairs 🚀🌌

> *Memory is the mind's playground! Test your recall across the solar system.*

---

---

## ✨ Overview

**Planetary Pairs** is a memory-matching game built in Python, featuring a **4×4 card grid** with **solar system imagery**. Players compete to match pairs of planets as fast as possible, battling their own records and a cumulative high-score leaderboard. Perfect for both gameplay and demonstrating GUI development in Python!

---

## 📖 Table of Contents

* [Features](#-features)
* [How It's Made](#-how-its-made)
* [Gameplay](#-gameplay)
* [Project Structure](#-project-structure)
* [Installation & Usage](#-installation--usage)
* [High-Score Mechanics](#-high-score-mechanics)
* [Architecture & Code Breakdown](#-architecture--code-breakdown)
* [Testing & Debugging](#-testing--debugging)
* [Future Enhancements](#-future-enhancements)
* [Contributing](#-contributing)
* [License](#-license)

---

## 🎮 Features

* **🖼️ 4×4 Planet Grid**: 8 unique planet images (2 copies each), randomized per session.
* **⏲️ Timer & Move Counter**: Real-time display of elapsed time and move count.
* **🏆 High-Score Leaderboard**: Persists top scores (`record.csv`) with player name, moves, and time.
* **📋 Instructions Popup**: Accessible in-game via **How to Play** button.
* **🎵 Audio Feedback**: Match chimes & victory jingle via **pygame.mixer**.
* **🔧 Customizable**: Easy to swap images and sounds; update themes by replacing the `images/` and `audio/` folders.

---

## 🔨 How It's Made

1. **Core Logic**: Uses Python’s \`\` to randomize card positions. Each card object holds:

   * \`\`: Unique identifier for matching logic.
   * \`\`: Front face (planet PNG), default back face image.
   * \`\`: `hidden`, `revealed`, or `matched`.

2. **GUI Layer**: Built with **Tkinter**:

   * \`\` class initializes root, menus, and game frames.
   * \`\` subclass of `tk.Button` manages click events & appearance.
   * Layout uses \`\` manager for flexible resizing.

3. **Event Handling**:

   * On click, check if less than 2 cards are currently `revealed`.
   * Reveal card image and append to `open_cards` list.
   * If two cards are open, schedule a \`\`:

     * If IDs match, mark both as `matched`, play **match sound**.
     * Else, flip both back and increment move counter.
   * When all pairs matched:

     * Stop timer, play **victory sound**, prompt for name entry and record score.

4. **Audio Integration**: Leveraged **pygame.mixer** for non-blocking sound playback:

   ```python
   pygame.mixer.init()
   match_sound = pygame.mixer.Sound('audio/match.mp3')
   victory_sound = pygame.mixer.Sound('audio/victory.mp3')
   ```

5. **Data Persistence**: Utilized Python’s \`\` module:

   * On game end, append `[player_name, moves, MM:SS]` to `record.csv`.
   * ` button reads CSV and displays results in a sortable **Tkinter **`.

---

## 🕹️ Gameplay

1. Click **New Game** → Enter your name.
2. All cards start **face-down**.
3. Click two cards:

   * ✅ **Match**: Cards stay face-up; score increments.
   * ❌ **Mismatch**: Cards flip back after 0.8s.
4. Continue until all **8 pairs** are matched.
5. **Moves** and **Time** metrics displayed.
6. Upon completion, your score is recorded; view **History** anytime.

> 🎯 **Goal**: Achieve the fastest time with the fewest moves to top the leaderboard!

---

## 💻 Installation & Running the Game

### Prerequisites

Make sure you have **Python 3.10+** installed.

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Game

```bash
python main.py
```

> 📝 Note: Ensure your working directory has the `images/`, `audio/`, and `record.csv` files alongside `main.py`.

---

## 📂 Project Structure

```bash
planetary-pairs/
├── audio/                # match.mp3, victory.mp3
├── images/               # planet_[1-8].png, back.png
├── main.py               # entry point & game logic
├── record.csv            # auto-generated scoreboard history
├── requirements.txt      # pip dependencies
├── LICENSE               # MIT license
└── README.md             # this document
```

---

## 🛠️ Architecture & Code Breakdown

| Component        | Responsibility                                          |
| ---------------- | ------------------------------------------------------- |
| **main.py**      | Bootstraps application, initializes `MainWindow`        |
| **MainWindow**   | Manages layout, menus, start/end operations             |
| **CardButton**   | Extends `tk.Button`; tracks state & image swapping      |
| **GameState**    | Holds dynamic variables: `open_cards`, `moves`, `timer` |
| **AudioManager** | Plays sounds asynchronously via `pygame.mixer`          |
| **CSVHandler**   | Read/write operations for high-score persistence        |

---

## 🔍 Testing & Debugging

* **Unit Tests**: Added simple tests for shuffle reproducibility & `check_match` logic using **unittest**.
* **Logging**: `logging` module reports state changes; helpful for debugging card state transitions.
* **Exception Handling**: Ensured robust file I/O: catches `FileNotFoundError` for missing `record.csv` and auto-creates.

---

## 🚧 Future Enhancements

* **Difficulty Levels**: 4×4 (easy), 6×6 (medium), 8×8 (hard) grids.
* **Online Leaderboards**: Integrate with Firebase or REST API.
* **Themes**: Support multiple card themes (animals, flags, emojis).
* **AI Opponent**: Single-player vs CPU challenge with adjustable memory AI.
* **Mobile Support**: Port to Kivy for cross-platform deployment.

---

## 🤝 Contributers

* **Ayush Patel** (BT2024054)
* **Kanav Kumar** (BT2024021)


### 📝 Code Style

* Follow **PEP8** guidelines.
* Docstrings for all public methods.
* Use **type hints** and static analysis via **mypy**.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

### 🌟 Ready to explore and match the cosmos? **Clone**, **run**, and conquer the leaderboard! 🌟
