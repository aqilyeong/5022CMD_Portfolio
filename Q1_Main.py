import time
from Q1_Medicine import Medicine
from Q1_Hash_table import LinearProbeHashTable

# ==========================================
# 2. Performance Comparison (Part 4)
# ==========================================

def linear_search_array(arr, key):
    """Standard sequential search for a 1D array."""
    for item in arr:
        if item.product_id == key:
            return item
    return None


def benchmark_performance():
    """
    Compares search execution time between Hash Table (Linear Probing)
    and a 1D Array (Linear Search) across multiple keys and multiple trials.
    """
    print("\n" + "=" * 60)
    print("       PERFORMANCE BENCHMARK: Hash Table vs 1D Array")
    print("=" * 60)

    TABLE_SIZE = 10000
    NUM_RECORDS = 5000
    NUM_TRIALS = 5  # Repeat each search N times and average — reduces noise

    hash_table = LinearProbeHashTable(TABLE_SIZE)
    array_1d = []

    print(f"  Loading {NUM_RECORDS} records into both structures...")
    for i in range(NUM_RECORDS):
        med = Medicine(f"MED{i}", f"Drug{i}", "tablets", 10.0, 100)
        hash_table.insert(med.product_id, med)
        array_1d.append(med)

    # Mix of existing (best/mid/worst case positions) and non-existing keys
    test_keys = [
        ("MED0",     "Existing — near start (best case for array)"),
        ("MED2499",  "Existing — middle of array"),
        ("MED4999",  "Existing — end of array (worst case for array)"),
        ("MED99999", "Non-existing"),
        ("MED55555", "Non-existing"),
    ]

    print(f"\n  {'Key':<12} {'Description':<48} {'Hash Table (ns)':>16} {'1D Array (ns)':>14} {'Speedup':>8}")
    print("  " + "-" * 102)

    for key, description in test_keys:
        # Average over NUM_TRIALS to reduce timing noise
        ht_times = []
        arr_times = []
        for _ in range(NUM_TRIALS):
            t0 = time.perf_counter_ns()
            hash_table.search(key)
            ht_times.append(time.perf_counter_ns() - t0)

            t0 = time.perf_counter_ns()
            linear_search_array(array_1d, key)
            arr_times.append(time.perf_counter_ns() - t0)

        ht_avg = sum(ht_times) // NUM_TRIALS
        arr_avg = sum(arr_times) // NUM_TRIALS
        speedup = f"~{arr_avg // ht_avg}x" if ht_avg > 0 and arr_avg > ht_avg else "similar"

        print(f"  {key:<12} {description:<48} {ht_avg:>16,} {arr_avg:>14,} {speedup:>8}")

    print("  " + "-" * 102)
    print("\n  ANALYSIS:")
    print("  Hash Table achieves O(1) average search via direct index computation.")
    print("  1D Array requires O(n) linear scan — time grows with dataset size.")
    print("  The difference is most visible for keys near the end or non-existing keys.")
    print("=" * 60 + "\n")


# ==========================================
# 3. Command-Line Interface (Part 3)
# ==========================================

def main():
    # Initialize system with a prime number size to reduce collisions
    inventory = LinearProbeHashTable(size=17)

    # Pre-populate sample data (Part 2)
    sample_data = [
        Medicine("M001", "Paracetamol", "tablets", 5.99, 150),
        Medicine("M002", "CoughEx", "syrup", 8.50, 45),
        Medicine("M003", "Vitamin C", "supplements", 15.00, 200),
        Medicine("M004", "Ibuprofen", "tablets", 7.20, 80)
    ]
    for med in sample_data:
        inventory.insert(med.product_id, med)

    while True:
        print("\n" + "=" * 42)
        print("   LOCAL PHARMACY INVENTORY SYSTEM")
        print("=" * 42)
        print("  1. Display All Products")
        print("  2. Search Product")
        print("  3. Insert New Product")
        print("  4. Run Performance Benchmark")
        print("  5. Exit")
        print("=" * 42)

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\n--- Current Inventory ---")
            inventory.display_all()

        elif choice == '2':
            key = input("Enter Product ID to search (e.g., M001): ").strip().upper()
            result = inventory.search(key)
            if result:
                print("\n  +----- Product Found -----+")
                print(f"  | ID    : {result.product_id}")
                print(f"  | Name  : {result.name}")
                print(f"  | Type  : {result.item_type}")
                print(f"  | Price : ${result.price:.2f}")
                print(f"  | Stock : {result.stock} units")
                print("  +-------------------------+")
            else:
                print(f"\n  Product '{key}' not found in inventory.")

        elif choice == '3':
            try:
                p_id = input("Enter Product ID: ").strip().upper()
                name = input("Enter Product Name: ").strip()
                p_type = input("Enter Product Type (e.g., tablets, syrup): ").strip()
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock Quantity: "))

                new_med = Medicine(p_id, name, p_type, price, stock)
                if inventory.insert(p_id, new_med):
                    print("\n  Product successfully added!")
                    stats = inventory.get_stats()
                    print(f"  Load Factor: {stats['load_factor']} | "
                          f"Collisions: {stats['total_collisions']}")
                    if inventory.load_factor() > 0.7:
                        print("  WARNING: Table is over 70% full. Consider a larger table size.")
            except ValueError:
                print("\nInvalid input for price or stock. Please enter numbers.")

        elif choice == '4':
            benchmark_performance()

        elif choice == '5':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()