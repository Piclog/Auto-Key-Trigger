import time

class StopWatch:
    def __init__(self):
        self._start_time = None
        self._elapsed = 0
        self._running = False

    def start(self, start_now=True):
        if start_now and not self._running:
            self._start_time = time.perf_counter()
            self._running = True

    def stop(self):
        if self._running:
            self._elapsed = time.perf_counter() - self._start_time
            self._running = False
            self._start_time = None

    def reset(self):
        self._start_time = None
        self._elapsed = 0
        self._running = False

    def elapsed(self):
        if self._running:
            return time.perf_counter() - self._start_time
        return self._elapsed
