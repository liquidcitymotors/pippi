import random
import time
from pippi import dsp, oscs, tune

start_time = time.time()

out = dsp.buffer()
freqs = tune.fromdegrees([2,5,8,9], octave=1, root='d')

for _ in range(100):
    pos = random.randint(0, 44100 * 30)
    pos = 0
    #length = random.randint(1, 44100 * 8)
    length = 44100 * 60 * 18

    # Pulsar wavetable constructed from a random set of linearly interpolated points & a randomly selected window
    # Frequency modulated between 1% and 300% with a randomly generated wavetable LFO between 0.01hz and 30hz
    # with a random, fixed-per-note pulsewidth
    wavetable = [0] + [ random.triangular(-1, 1) for _ in range(random.randint(3, 20)) ] + [0]
    mod = [ random.triangular(0, 1) for _ in range(random.randint(3, 20)) ]
    osc = oscs.Osc(wavetable=wavetable, window='random', mod=mod)
    osc.pulsewidth = random.random()

    osc.freq = random.choice(freqs) * 2**random.randint(0, 3)
    osc.mod_freq = random.triangular(0.01, 30)
    osc.mod_range = random.triangular(0, random.choice([0.03, 0.02, 0.01, 3]))
    osc.amp = random.triangular(0.05, 0.2)
    osc.amp = random.triangular(0.005, 0.02)

    if osc.mod_range > 1:
        osc.amp *= 0.5

    note = osc.play(length)
    note = note.env(random.choice(['sine', 'phasor', 'line']))
    note = note.env('random')
    note = note.pan(random.random())

    out.dub(note, pos)

out.write('pulsar_synth.wav')
elapsed_time = time.time() - start_time
print('Render time: %s seconds' % round(elapsed_time, 2))
print('Output length: %s seconds' % round(len(out)/44100, 2))