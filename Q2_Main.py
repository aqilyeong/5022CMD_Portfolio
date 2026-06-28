import time
from Q2_Transaction import Transaction
from Q2_Merge_sort import merge_sort
from Q2_Search import binary_search, linear_search

# ==========================================
# Dataset — 15 unsorted transaction records
# ==========================================

def _get_initial_dataset() -> list:
    """Returns the initial unsorted dataset stored in a one-dimensional list."""
    return [
        Transaction("T007", "Alice Tan",  "Laptop",        2499.00, "2025-03-15"),
        Transaction("T002", "Bob Lim",    "Headphones",     149.90, "2025-01-20"),
        Transaction("T013", "Carol Wong", "Desk Chair",     599.00, "2025-05-02"),
        Transaction("T001", "David Lee",  "Mouse",           45.00, "2025-01-10"),
        Transaction("T010", "Eve Ng",     "Monitor",        899.00, "2025-04-11"),
        Transaction("T005", "Frank Tan",  "Keyboard",       129.00, "2025-02-28"),
        Transaction("T014", "Grace Lim",  "Webcam",          89.90, "2025-05-18"),
        Transaction("T003", "Henry Ong",  "USB Hub",         39.00, "2025-01-25"),
        Transaction("T011", "Iris Chan",  "Tablet",         749.00, "2025-04-19"),
        Transaction("T008", "James Yap",  "Printer",        399.00, "2025-03-22"),
        Transaction("T015", "Karen Ho",   "SSD 1TB",        189.00, "2025-06-01"),
        Transaction("T004", "Leo Tan",    "Mousepad",        25.00, "2025-02-05"),
        Transaction("T009", "Mia Lim",    "Speaker",        259.00, "2025-04-03"),
        Transaction("T006", "Nathan Ng",  "Microphone",     199.00, "2025-03-08"),
        Transaction("T012", "Olivia Tay", "Gaming Chair",   899.00, "2025-04-28"),
    ]


# ==========================================
# Display Helpers
# ==========================================

def display_transactions(transactions: list, title: str = "Transactions") -> None:
    """Prints all transactions in a formatted aligned table."""
    header  = f"  {'#':<5} {'ID':<6} {'Customer':<16} {'Product':<18} {'Amount':>10} {'Date':<12}"
    divider = "  " + "-" * 71

    print(f"\n  {'=' * 71}")
    print(f"  {title.center(71)}")
    print(f"  {'=' * 71}")
    print(header)
    print(divider)

    for idx, t in enumerate(transactions, 1):
        print(f"  {idx:<5} {t.transaction_id:<6} {t.customer_name:<16} "
              f"{t.product_name:<18} ${t.amount:>9.2f} {t.transaction_date:<12}")

    print(divider)
    print(f"  Total records: {len(transactions)}\n")


def display_transaction_detail(t: Transaction) -> None:
    """Prints a single transaction as a detail card."""
    print("  +---------- Transaction Found ----------+")
    print(f"  | ID       : {t.transaction_id}")
    print(f"  | Customer : {t.customer_name}")
    print(f"  | Product  : {t.product_name}")
    print(f"  | Amount   : ${t.amount:.2f}")
    print(f"  | Date     : {t.transaction_date}")
    print("  +---------------------------------------+\n")


# ==========================================
# Feature Handlers
# ==========================================

def handle_sort_by_id(transactions: list) -> list:
    """Mandatory (b): Sorts by transactionID using Merge Sort. Shows before/after + call count."""
    display_transactions(transactions, "BEFORE SORTING (Original Order)")

    call_counter = [0]
    start        = time.perf_counter_ns()
    sorted_list  = merge_sort(transactions,
                              key_func=lambda x: x.transaction_id,
                              call_counter=call_counter)
    elapsed      = time.perf_counter_ns() - start

    display_transactions(sorted_list, "AFTER SORTING (Sorted by Transaction ID)")
    print(f"  Recursive calls made : {call_counter[0]}")
    print(f"  Time taken           : {elapsed:,} nanoseconds\n")
    return sorted_list


def handle_binary_search(transactions: list, is_sorted_by_id: bool) -> None:
    """Mandatory (c): Searches by ID using Binary Search. Requires list sorted by ID."""
    if not is_sorted_by_id:
        print("\n  [!] Binary Search requires the list sorted by Transaction ID.")
        print("  [!] Please use option 2 to sort first.\n")
        return

    target = input("\n  Enter Transaction ID to search (e.g., T005): ").strip().upper()
    result, comparisons = binary_search(transactions, target)

    print(f"\n  Binary Search — searching for '{target}':")
    print(f"  Comparisons made: {comparisons}")
    if result:
        display_transaction_detail(result)
    else:
        print(f"  Transaction '{target}' was NOT found in the records.\n")


def handle_linear_search(transactions: list) -> None:
    """Mandatory (d): Searches by ID using Linear Search. Works on unsorted list."""
    target = input("\n  Enter Transaction ID to search (e.g., T005): ").strip().upper()
    result, comparisons = linear_search(transactions, target)

    print(f"\n  Linear Search — searching for '{target}':")
    print(f"  Comparisons made: {comparisons}")
    if result:
        display_transaction_detail(result)
    else:
        print(f"  Transaction '{target}' was NOT found in the records.\n")


def handle_insert(transactions: list) -> list:
    """Advanced (a): Allows dynamic insertion of a new transaction."""
    print("\n  --- Insert New Transaction ---")
    try:
        t_id   = input("  Transaction ID (e.g., T016) : ").strip()
        cname  = input("  Customer Name               : ").strip()
        pname  = input("  Product Name                : ").strip()
        amount = float(input("  Amount                      : "))
        date   = input("  Date (YYYY-MM-DD)           : ").strip()

        transactions.append(Transaction(t_id, cname, pname, amount, date))
        print(f"\n  Transaction '{t_id.upper()}' added successfully.")
        print("  Note: List is now unsorted. Re-sort if Binary Search is needed.\n")
    except ValueError as e:
        print(f"\n  Invalid input: {e}\n")
    return transactions


def handle_sort_by_attribute(transactions: list) -> tuple:
    """Advanced (b): Sorts by a user-chosen attribute using Merge Sort."""
    print("\n  Sort by which attribute?")
    print("  1. Amount (ascending)")
    print("  2. Transaction Date (ascending)")
    attr_choice = input("  Enter choice (1-2): ").strip()

    if attr_choice == '1':
        key_func  = lambda x: x.amount
        label     = "Amount"
        attr_name = "amount"
    elif attr_choice == '2':
        key_func  = lambda x: x.transaction_date
        label     = "Transaction Date"
        attr_name = "date"
    else:
        print("  Invalid choice.\n")
        return transactions, None

    display_transactions(transactions, "BEFORE SORTING")

    call_counter = [0]
    start        = time.perf_counter_ns()
    sorted_list  = merge_sort(transactions, key_func=key_func, call_counter=call_counter)
    elapsed      = time.perf_counter_ns() - start

    display_transactions(sorted_list, f"AFTER SORTING (Sorted by {label})")
    print(f"  Recursive calls made : {call_counter[0]}")
    print(f"  Time taken           : {elapsed:,} nanoseconds\n")
    return sorted_list, attr_name


def handle_benchmark(transactions: list) -> None:
    """Q2.4c: Measures and compares execution time of Merge Sort vs Binary Search."""
    print("\n" + "=" * 65)
    print("  PERFORMANCE BENCHMARK: Merge Sort vs Binary Search")
    print("=" * 65)

    NUM_TRIALS = 5

    # Time Merge Sort over multiple trials to reduce noise
    sort_times = []
    for _ in range(NUM_TRIALS):
        t0 = time.perf_counter_ns()
        merge_sort(transactions, key_func=lambda x: x.transaction_id)
        sort_times.append(time.perf_counter_ns() - t0)
    sort_avg = sum(sort_times) // NUM_TRIALS

    # Prepare sorted list for Binary Search timing
    sorted_list = merge_sort(transactions, key_func=lambda x: x.transaction_id)

    # Time Binary Search across existing and non-existing keys
    search_keys = [("T005", "Existing"), ("T012", "Existing"),
                   ("T999", "Non-existing"), ("T000", "Non-existing")]
    bs_times = []
    for key, _ in search_keys:
        for _ in range(NUM_TRIALS):
            t0 = time.perf_counter_ns()
            binary_search(sorted_list, key)
            bs_times.append(time.perf_counter_ns() - t0)
    bs_avg = sum(bs_times) // len(bs_times)

    print(f"\n  {'Operation':<38} {'Avg Time (ns)':>14} {'Complexity':>12}")
    print("  " + "-" * 66)
    print(f"  {'Merge Sort (n=' + str(len(transactions)) + ')':<38} {sort_avg:>14,} {'O(n log n)':>12}")
    print(f"  {'Binary Search (avg, 4 keys x 5 trials)':<38} {bs_avg:>14,} {'O(log n)':>12}")
    print("  " + "-" * 66)
    print("\n  ANALYSIS:")
    print("  Merge Sort processes the entire list — time grows as O(n log n) with n.")
    print("  Binary Search targets one element — O(log n) is significantly faster per")
    print("  lookup, but REQUIRES the list to be pre-sorted to function correctly.")
    print("  Practical strategy: sort once with Merge Sort, then search many times fast.")
    print("=" * 65 + "\n")


def handle_complexity_table() -> None:
    """Advanced (d): Displays time complexity analysis in tabular format."""
    print("\n" + "=" * 67)
    print("  TIME COMPLEXITY ANALYSIS")
    print("=" * 67)
    print(f"  {'Algorithm':<20} {'Best':<12} {'Average':<14} {'Worst':<14} {'Space'}")
    print("  " + "-" * 67)
    print(f"  {'Merge Sort':<20} {'O(n log n)':<12} {'O(n log n)':<14} {'O(n log n)':<14} {'O(n)'}")
    print(f"  {'Binary Search':<20} {'O(1)':<12} {'O(log n)':<14} {'O(log n)':<14} {'O(1)'}")
    print(f"  {'Linear Search':<20} {'O(1)':<12} {'O(n)':<14} {'O(n)':<14} {'O(1)'}")
    print("  " + "-" * 67)
    print()
    print("  KEY OBSERVATIONS:")
    print("  - Merge Sort guarantees O(n log n) in ALL cases — no worst-case degradation.")
    print("  - Binary Search is O(log n) but requires a pre-sorted list.")
    print("  - Linear Search needs no sorting but degrades to O(n) on large datasets.")
    print("  - Optimal strategy: sort once with Merge Sort, then Binary Search for O(log n)")
    print("    lookups on every subsequent search.")
    print("=" * 67 + "\n")


# ==========================================
# Main Menu
# ==========================================

def main() -> None:
    transactions    = _get_initial_dataset()   # 1D list, initially unsorted
    is_sorted_by_id = False                    # Gate for Binary Search

    while True:
        print("\n" + "=" * 47)
        print("     TRANSACTION MANAGEMENT SYSTEM")
        print("=" * 47)
        print("  -- Mandatory Features --")
        print("  1. Display All Transactions")
        print("  2. Sort by Transaction ID (Merge Sort)")
        print("  3. Search by ID (Binary Search)")
        print("  4. Search by ID (Linear Search)")
        print("  -- Advanced Features --")
        print("  5. Insert New Transaction")
        print("  6. Sort by Different Attribute")
        print("  7. Performance Benchmark")
        print("  8. Time Complexity Analysis")
        print("  0. Exit")
        print("=" * 47)
        print(f"  [Sort status: {'Sorted by ID ✓' if is_sorted_by_id else 'Unsorted'}]")

        choice = input("  Enter choice (0-8): ").strip()

        if choice == '1':
            display_transactions(transactions, "ALL TRANSACTIONS")

        elif choice == '2':
            transactions    = handle_sort_by_id(transactions)
            is_sorted_by_id = True

        elif choice == '3':
            handle_binary_search(transactions, is_sorted_by_id)

        elif choice == '4':
            handle_linear_search(transactions)

        elif choice == '5':
            transactions    = handle_insert(transactions)
            is_sorted_by_id = False   # New record invalidates sort order

        elif choice == '6':
            transactions, attr = handle_sort_by_attribute(transactions)
            # Binary search gate only stays true if sorted specifically by ID
            is_sorted_by_id = (attr == "transaction_id")

        elif choice == '7':
            handle_benchmark(transactions)

        elif choice == '8':
            handle_complexity_table()

        elif choice == '0':
            print("\n  Exiting system. Goodbye!\n")
            break

        else:
            print("\n  Invalid choice. Please enter 0-8.\n")


if __name__ == "__main__":
    main()