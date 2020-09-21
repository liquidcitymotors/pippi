#cython: language_level=3

from pippi.soundbuffer cimport SoundBuffer
from pippi.wavetables cimport Wavetable
cimport numpy as np

cpdef np.ndarray flatten(SoundBuffer snd)
cpdef Wavetable bandwidth(SoundBuffer snd, int winsize=*)
cpdef Wavetable flatness(SoundBuffer snd, int winsize=*)
cpdef Wavetable rolloff(SoundBuffer snd, int winsize=*)
cpdef Wavetable centroid(SoundBuffer snd, int winsize=*)
cpdef Wavetable contrast(SoundBuffer snd, int winsize=*)
cpdef Wavetable pitch(SoundBuffer snd, double tolerance=*, int winsize=*, int hopsize=*, bint backfill=*)
cpdef list onsets(SoundBuffer snd, str method=*, int winsize=*, int hopsize=*, bint seconds=*)
cpdef list segments(SoundBuffer snd, str method=*, int winsize=*, int hopsize=*)

