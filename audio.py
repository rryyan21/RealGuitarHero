import numpy as np
import sounddevice as sd
import librosa

SAMPLE_RATE = 22050
BLOCK_SEC = 0.4

# Configure default audio I/O for predictable behavior
sd.default.samplerate = SAMPLE_RATE
sd.default.channels = 1

def record_block(seconds=BLOCK_SEC, sr=SAMPLE_RATE):
    audio = sd.rec(int(seconds*sr), samplerate=sr, channels=1, dtype='float32')
    sd.wait()
    return audio[:,0]

def chroma_from_block(block, sr=SAMPLE_RATE):
    chroma = librosa.feature.chroma_cqt(y=block, sr=sr)
    chroma = np.maximum(chroma, 0)
    chroma = chroma.mean(axis=1)
    s = chroma.sum()
    if s > 0:
        chroma = chroma / s
    return chroma

def chord_score(chroma, chord_pitch_classes):
    return float(sum(chroma[p] for p in chord_pitch_classes))

def guess_chord_mvp(block, chords_dict):
    chroma = chroma_from_block(block)
    best_name, best_s = None, -1e9
    for name, pcs in chords_dict.items():
        s = chord_score(chroma, pcs)
        if s > best_s:
            best_name, best_s = name, s
    return best_name

def warmup_audio_and_librosa():
    """Prime mic permissions and heavy librosa imports to avoid mid-game stalls."""
    try:
        # Trigger mic permission prompt and initialize the device
        _ = sd.rec(int(0.05 * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
        sd.wait()
    except Exception:
        # Non-fatal if device not ready; gameplay can proceed and retry later
        pass
    try:
        # Trigger lazy imports and JIT warmup in librosa/numba
        silent = np.zeros(int(0.1 * SAMPLE_RATE), dtype=np.float32)
        _ = librosa.feature.chroma_cqt(y=silent, sr=SAMPLE_RATE)
    except Exception:
        pass

