# 🎤 Colorful Karaoke Display

A Python script that displays song lyrics line-by-line with colorful text in the terminal.

## Features

- Displays lyrics with timing delays
- Each line appears in a different color
- Uses the Rich library for beautiful terminal output
- Cycles through 14 different colors automatically

## Installation

1. Make sure you have Python installed
2. Install the Rich library:
   ```bash
   pip install rich
   ```
3. Run the script:
   ```bash
   python karaoke.py
   ```

## How it works

The script takes a list of lyrics and displays them one by one with:
- A 0.1 second delay between lines
- Automatic color cycling (red → blue → green → yellow, etc.)
- Text wrapping for long lines

## Customization

You can easily customize:
- **Timing**: Change `time.sleep(0.1)` to speed up or slow down
- **Colors**: Modify the `colors` list to use different colors
- **Lyrics**: Replace the `lyrics` list with your own song

## Future Ideas

- [ ] Add multiple songs
- [ ] Let users choose display speed
- [ ] Add sound synchronization
- [ ] Create a simple menu system
- [ ] Support for loading lyrics from files

## Requirements

- Python 3.6+
- Rich library (`pip install rich`)

---

A fun little project to practice Python basics and terminal styling!
