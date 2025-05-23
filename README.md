# Planetary Pairs 🚀🌌

> *Memory is the mind's playground! Test your recall across the solar system.*
![Logo](game-images/logo.jpeg)

---

---

## ✨ Overview

**Planetary Pairs** is a memory-matching game built in Python, featuring a **4×4 card grid** with **solar system imagery**. Players compete to match pairs of planets as fast as possible, battling their own records and a cumulative high-score leaderboard. Perfect for both gameplay and demonstrating GUI development in Python!

---

## 📖 Table of Contents

* [Features](#-features)
* [Game Screenshots](#-game-screenshots)
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

## 🖼️ Game Screenshots

Here are some screenshots from our game to give you a quick look at the gameplay and interface:

| Home Page | Enter Name Page | Memory Game |
|--------------|--------------|--------------|
| ![Home Page](game-images/Home-Page.png) | ![Enter Name Page](game-images/Enter-Name-Page.png) | ![Memory Game](game-images/Memory-Game.png) |

| Scores Page | Exit Page | How To Play |
|--------------|--------------|--------------|
| ![Scores Page](game-images/Scores-Page.png) | ![Exit Page](game-images/Exit-Page.png) | ![How To Play](game-images/How-To-Play-Page.png) |

---

## 🔨 How It's Made

1. **Core Logic**: Uses Python’s `random` module to randomize card positions. Each card object holds:

   * `id`: Unique identifier for matching logic.
   * `front_image`: Front face (planet PNG), default back face image.
   * `state`: `hidden`, `revealed`, or `matched`.

2. **GUI Layer**: Built with **Tkinter**:

   * `MemoryGame` class initializes root, menus, and game frames.
   * `CardButton` subclass of `tk.Button` manages click events & appearance.
   * Layout uses `grid()` manager for flexible resizing.

3. **Event Handling**:

   * On click, check if less than 2 cards are currently `revealed`.
   * Reveal card image and append to `open_cards` list.
   * If two cards are open, schedule a `root.after()`:

     * If IDs match, mark both as `matched`, play **match sound**.
     * Else, flip both back and increment move counter.
   * When all pairs matched:

     * Stop timer, play **victory sound**, prompt for name entry and record score.

4. **Audio Integration**: Leveraged **pygame.mixer** for non-blocking sound playback:

   ```python
   pygame.mixer.init()
   match_sound = pygame.mixer.Sound('audio/match.mp3')
   victory_sound = pygame.mixer.Sound('audio/victory.mp3')
   
5. Data Persistence: Utilized Python’s csv module:

   * On game end, append [player_name, moves, MM:SS] to record.csv.

   * view_history() button reads CSV and displays results in a sortable Tkinter Treeview.

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

### Required Directory

For Windows 
```bash
cd Windows
```
For MacOS
```bash
cd MacOS
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Game

```bash
python main.py
```

> 📝 Note: Ensure your working directory has the `images/`, `audio/` and `record.csv` files alongside `main.py`.

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

## 🤝 Contributors

| Name | GitHub | LinkedIn | Instagram |
|------|--------|----------|-----------|
| **Ayush Patel** (BT2024054) | [Ayush-patel9](https://github.com/Ayush-patel9) | [Ayush Patel](https://www.linkedin.com/in/ayush-patel-72a037316) | [ayush.p_9/](https://www.instagram.com/ayush.p_9/) |
| **Kanav Kumar** (BT2024021) | [KINGKK-007](https://github.com/KINGKK-007) | [Kanav Kumar](https://www.linkedin.com/in/kanav-kumar-b655962b5/) | [kanavvkumarr](https://www.instagram.com/kanavvkumarr/) |

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

### 🌟 Ready to explore and match the cosmos? **Clone**, **run**, and conquer the leaderboard! 🌟
