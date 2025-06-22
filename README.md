# MiniTaskTracker

MiniTaskTracker is a terminal-based task management application written in Python. It allows users to add, remove, edit, and display tasks with simple interactive prompts. Tasks are stored in JSON and can be prioritized or sorted by deadline. All data is persistent between sessions.

---

## 🧠 Features

- 📅 Add tasks with:
  - Name
  - Start date (`YYYY-MM-DD` or `"current"`)
  - Deadline (`YYYY-MM-DD-HH`)
  - Priority (High, Medium, Low)

- ✏️ Edit any part of an existing task
- 🗑️ Remove tasks
- 🗃️ Save/load from a configurable JSON file
- ⚙️ Settings menu:
  - Sorting by priority or timeline
  - Toggle display on program entry
  - Change task storage filename

- 📄 Persistent config stored in `preferences.json`

---

## 📁 File Structure

```
MiniTaskTracker/
├── Source/
│   ├── Main.py         # Main application loop and UI
│   └── Manipulator.py  # All task loading, saving, and displaying logic
├── tasks.json          # Default task storage file
└── preferences.json    # Stores display and sorting settings
```

---

## 🛠️ How to Run

1. Install Python 3.10+
2. Clone or download this repo
3. Run the main script:
   ```bash
   python Source/Main.py
   ```

---

## 📌 Notes

- Dates must be formatted as `YYYY-MM-DD-HH` (year-month-day-hour, 24hr format).
- Sorting by timeline uses `datetime` delta comparisons.
- Code is currently **not GUI-based**. A GUI version may come in a future version.
- UX is stable and won't break on bad input (anymore 😤).