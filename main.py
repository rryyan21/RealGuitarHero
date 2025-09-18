import json, time, pygame
from visuals import UI
from notes import Note
from audio import record_block, guess_chord_mvp
from chords import CHORDS

SPAWN_EVERY_SEC = 1.2

def load_song(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data["sequence"]

def main():
    pygame.init()
    ui = UI()
    running = True

    seq = load_song("songs/simple_c_g_am_f.json")
    notes = []
    last_spawn = 0.0
    song_t = 0.0

    score, combo = 0, 0
    last_status = "Ready"
    next_index = 0
    expected = seq[0] if seq else ""

    prev_time = time.time()

    while running:
        now = time.time()
        dt = now - prev_time
        prev_time = now
        song_t += dt

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        if next_index < len(seq) and (song_t - last_spawn) >= SPAWN_EVERY_SEC:
            notes.append(Note(seq[next_index], spawn_time=song_t, speed=260))
            last_spawn = song_t
            next_index += 1

        for n in notes:
            n.update(dt)

        for n in notes:
            if n.active and not n.judged and n.in_hit_window(window=18):
                block = record_block(0.35)
                guess = guess_chord_mvp(block, CHORDS)
                n.judged = True
                expected = n.chord
                if guess == n.chord:
                    n.hit = True
                    score += 100 + 10*combo
                    combo += 1
                    last_status = f"Hit {guess}"
                else:
                    combo = 0
                    last_status = f"Miss. You played {guess}"

        notes = [n for n in notes if n.y < 640 and n.active]
        ui.draw_frame(notes, score, combo, last_status, expected)
        ui.clock.tick(60)

if __name__ == "__main__":
    main()

