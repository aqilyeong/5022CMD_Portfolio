import threading
import time
from Q3_Factorial import factorial

# ==========================================
# Factorial Worker Thread (Q3 #3)
# ==========================================

class FactorialThread(threading.Thread):
    """
    A worker thread that computes the factorial of ONE number.

    Each thread records its OWN start and end timestamps so the overall
    elapsed time can be derived as (latest end - earliest start) across
    all threads — matching the formula required by the brief:

        T = End_Time_Of_Thread_Finished_Last - Start_Time_Of_Thread_Started_First
    """

    # Class-level lock shared by ALL instances. Guards writes to the shared
    # results store so concurrent threads cannot corrupt it (data consistency).
    _results_lock = threading.Lock()

    def __init__(self, number: int, results: dict):
        super().__init__()
        self.number     = number
        self.results    = results   # shared dict, written under the lock below
        self.start_time = None      # this thread's individual start (ns)
        self.end_time   = None      # this thread's individual end   (ns)

    def run(self) -> None:
        """Executed automatically when .start() is called on the thread."""
        # Stamp the moment THIS thread begins its work
        self.start_time = time.perf_counter_ns()

        value = factorial(self.number)   # the actual CPU-bound computation

        # Stamp the moment THIS thread finishes its work
        self.end_time = time.perf_counter_ns()

        # --- Critical Section ---
        # Multiple threads may finish near-simultaneously and write to the same
        # dict. The lock serialises these writes so no update is lost or
        # interleaved — this is how data consistency is preserved (LO4).
        with FactorialThread._results_lock:
            self.results[self.number] = value