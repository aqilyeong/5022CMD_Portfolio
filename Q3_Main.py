import time
from Q3_Factorial import factorial
from Q3_Worker import FactorialThread

# ==========================================
# Experiment Configuration
# ==========================================

NUMBERS = [50, 100, 200]   # the three factorials required by the brief
ROUNDS  = 10               # 10 test rounds required by the brief


# ==========================================
# A single MULTITHREADED round (Q3 #3)
# ==========================================

def run_multithreaded_round(numbers: list) -> int:
    """
    Computes all factorials using one dedicated thread per number.
    Returns T (nanoseconds) = latest thread end - earliest thread start.
    """
    results = {}
    threads = [FactorialThread(n, results) for n in numbers]

    # Launch all threads — each begins running concurrently
    for t in threads:
        t.start()

    # Block until every thread has completed its work
    for t in threads:
        t.join()

    # Apply the brief's formula exactly:
    #   t1 = start time of the thread that STARTED first  (minimum start)
    #   t2 = end   time of the thread that FINISHED last  (maximum end)
    t1 = min(t.start_time for t in threads)
    t2 = max(t.end_time   for t in threads)
    return t2 - t1


# ==========================================
# A single SINGLE-THREADED round (Q3 #4)
# ==========================================

def run_singlethreaded_round(numbers: list) -> int:
    """
    Computes the same factorials sequentially (no threads).
    Returns total time (nanoseconds) from first computation to last.
    """
    start = time.perf_counter_ns()       # t1: before the first computation
    results = {}
    for n in numbers:
        results[n] = factorial(n)        # compute one after another
    end = time.perf_counter_ns()         # t2: after the last computation
    return end - start


# ==========================================
# Experiment Runners (10 rounds + averages)
# ==========================================

def run_multithreaded_experiment() -> list:
    """Runs the multithreaded experiment for ROUNDS rounds, prints per-round T."""
    print("\n" + "=" * 52)
    print("   MULTITHREADED EXPERIMENT (3 threads, 1 per number)")
    print("=" * 52)
    print(f"  {'Round':<8} {'T = t2 - t1 (nanoseconds)':>30}")
    print("  " + "-" * 42)

    times = []
    for r in range(1, ROUNDS + 1):
        t = run_multithreaded_round(NUMBERS)
        times.append(t)
        print(f"  {r:<8} {t:>30,}")

    print("  " + "-" * 42)
    avg = sum(times) // ROUNDS
    print(f"  {'AVERAGE':<8} {avg:>30,}")
    print("=" * 52)
    return times


def run_singlethreaded_experiment() -> list:
    """Runs the single-threaded experiment for ROUNDS rounds, prints per-round T."""
    print("\n" + "=" * 52)
    print("   SINGLE-THREADED EXPERIMENT (sequential)")
    print("=" * 52)
    print(f"  {'Round':<8} {'Total time (nanoseconds)':>30}")
    print("  " + "-" * 42)

    times = []
    for r in range(1, ROUNDS + 1):
        t = run_singlethreaded_round(NUMBERS)
        times.append(t)
        print(f"  {r:<8} {t:>30,}")

    print("  " + "-" * 42)
    avg = sum(times) // ROUNDS
    print(f"  {'AVERAGE':<8} {avg:>30,}")
    print("=" * 52)
    return times


# ==========================================
# Full Comparison (Q3 #3 vs #4)
# ==========================================

def run_full_comparison() -> None:
    """Runs both experiments and prints a side-by-side comparison + analysis."""
    mt_times = run_multithreaded_experiment()
    st_times = run_singlethreaded_experiment()

    mt_avg = sum(mt_times) // ROUNDS
    st_avg = sum(st_times) // ROUNDS

    print("\n" + "=" * 64)
    print("   SIDE-BY-SIDE COMPARISON")
    print("=" * 64)
    print(f"  {'Round':<8} {'Multithreaded (ns)':>20} {'Single-Threaded (ns)':>22} {'Faster':>10}")
    print("  " + "-" * 62)
    for i in range(ROUNDS):
        faster = "Multi" if mt_times[i] < st_times[i] else "Single"
        print(f"  {i + 1:<8} {mt_times[i]:>20,} {st_times[i]:>22,} {faster:>10}")
    print("  " + "-" * 62)
    print(f"  {'AVG':<8} {mt_avg:>20,} {st_avg:>22,}")
    print("=" * 64)

    # Factual verdict only — leave the GIL discussion for your written report
    print("\n  RESULT:")
    if st_avg < mt_avg:
        diff = mt_avg - st_avg
        print(f"  Single-threaded was faster by {diff:,} ns on average.")
        print("  Multithreading did NOT shorten the time for this CPU-bound task.")
    else:
        diff = st_avg - mt_avg
        print(f"  Multithreaded was faster by {diff:,} ns on average.")
    print()


# ==========================================
# Result Verification (data-consistency proof)
# ==========================================

def show_result_info() -> None:
    """
    Verifies both methods produce identical results and shows digit counts
    (200! has hundreds of digits, so we show the size rather than the full value).
    """
    print("\n" + "=" * 52)
    print("   FACTORIAL RESULT VERIFICATION")
    print("=" * 52)
    print(f"  {'Number':<10} {'Digits in result':>20}")
    print("  " + "-" * 32)

    # Compute once sequentially, once via threads, then confirm they match
    seq = {n: factorial(n) for n in NUMBERS}

    thr_results = {}
    threads = [FactorialThread(n, thr_results) for n in NUMBERS]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    for n in NUMBERS:
        digits = len(str(seq[n]))
        print(f"  {n}!{'':<7} {digits:>20,}")

    consistent = (seq == thr_results)
    print("  " + "-" * 32)
    print(f"  Sequential vs threaded results identical: {consistent}")
    print("  (Confirms the lock preserved data consistency across threads.)")
    print("=" * 52 + "\n")


# ==========================================
# Menu
# ==========================================

def main() -> None:
    while True:
        print("\n" + "=" * 56)
        print("     FACTORIAL CONCURRENCY ANALYZER")
        print("=" * 56)
        print(f"  Computing factorials of: {NUMBERS}  |  Rounds: {ROUNDS}")
        print("  " + "-" * 52)
        print("  1. Run Multithreaded Experiment")
        print("  2. Run Single-Threaded Experiment")
        print("  3. Run Full Comparison (both + analysis)")
        print("  4. Verify Results & Show Digit Counts")
        print("  0. Exit")
        print("=" * 56)

        choice = input("  Enter choice (0-4): ").strip()

        if choice == '1':
            run_multithreaded_experiment()
        elif choice == '2':
            run_singlethreaded_experiment()
        elif choice == '3':
            run_full_comparison()
        elif choice == '4':
            show_result_info()
        elif choice == '0':
            print("\n  Exiting. Goodbye!\n")
            break
        else:
            print("\n  Invalid choice. Please enter 0-4.\n")


if __name__ == "__main__":
    main()