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
    """Compares execution time between Hash Table and 1D Array."""
    print("\n--- PERFORMANCE BENCHMARK ---")

    # Generate 5,000 mock records to make the time difference obvious
    table_size = 10000
    num_records = 5000

    hash_table = LinearProbeHashTable(table_size)
    array_1d = []

    print(f"Loading {num_records} records into both data structures...")
    for i in range(num_records):
        med = Medicine(f"MED{i}", f"Drug_{i}", "tablets", 10.0, 100)
        hash_table.insert(med.product_id, med)
        array_1d.append(med)

    # Test cases
    existing_key = "MED4999"  # Worst case for array (at the very end)
    non_existing_key = "MED99999"

    # Benchmark Hash Table
    start_time = time.perf_counter_ns()
    hash_table.search(existing_key)
    hash_table.search(non_existing_key)
    ht_time = time.perf_counter_ns() - start_time

    # Benchmark 1D Array
    start_time = time.perf_counter_ns()
    linear_search_array(array_1d, existing_key)
    linear_search_array(array_1d, non_existing_key)
    arr_time = time.perf_counter_ns() - start_time

    print(f"Hash Table Search Time: {ht_time:,} nanoseconds")
    print(f"1D Array Search Time:   {arr_time:,} nanoseconds")
    if ht_time < arr_time:
        print(f"Result: Hash Table is ~{arr_time // ht_time}x faster for this dataset.")
    print("-----------------------------\n")


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
        print("\n=== LOCAL PHARMACY INVENTORY SYSTEM ===")
        print("1. Display All Products")
        print("2. Search Product")
        print("3. Insert New Product")
        print("4. Run Performance Benchmark (Hash vs Array)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\n--- Current Inventory ---")
            inventory.display_all()

        elif choice == '2':
            key = input("Enter Product ID to search (e.g., M001): ").strip().upper()
            result = inventory.search(key)
            if result:
                print(f"\nProduct Found: {result}")
            else:
                print("\nProduct not found.")

        elif choice == '3':
            try:
                p_id = input("Enter Product ID: ").strip().upper()
                name = input("Enter Product Name: ").strip()
                p_type = input("Enter Product Type (e.g., tablets, syrup): ").strip()
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock Quantity: "))

                new_med = Medicine(p_id, name, p_type, price, stock)
                if inventory.insert(p_id, new_med):
                    print("\nProduct successfully added!")
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