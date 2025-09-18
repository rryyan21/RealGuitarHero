# Real Guitar Hero

Minimal rhythm game that listens to a real guitar. Four chords for MVP: C, G, Am, F.

## Setup

python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py

## How to play

- Strum only C, G, Am, F.
- Hit when the note crosses the line.
- Score and combo show at top left.

## Notes

- If detection is spotty, raise record window in `main.py` to 0.45.
- If latency feels slow, widen hit window to 24 or speed notes to 300.

Acceptance criteria

App launches to a window with one lane and falling labeled notes.

Mic input is read. When a note hits the line and the correct chord is played, the score increases and combo increments.

Status text shows last action: Hit <chord> or Miss.

No crashes on Mac or Windows with a default mic device.

Follow-ups after MVP

Rolling audio buffer for lower latency.

Multi-lane mode that maps each chord to a lane.

Backing track with precomputed timing.

Export a 20 second demo video and a GIF for the README.
