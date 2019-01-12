cdef class Osc:
    cdef public double[:] freq
    cdef public double[:] amp
    cdef public double[:] wavetable

    cdef public double phase

    cdef public int channels
    cdef public int samplerate
    cdef public int wtsize

    cdef object _play(self, int length)