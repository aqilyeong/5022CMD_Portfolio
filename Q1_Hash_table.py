from typing import Any
from typing import Optional, List
class HashEntry:
    """
    Represents a single bucket in the Hash Table.
    Using a key-value pair object (rather than a plain array) so the structure
    is self-describing and reusable across different value types.
    """

    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value


class LinearProbeHashTable:
    """
    Hash Table using Linear Probing (Open Addressing) for collision resolution.
    Collision resolution: when a slot is occupied, probe the next slot
    sequentially until an empty slot is found — O(1) average, O(n) worst case.
    """

    def __init__(self, size: int):
        self.size = size
        self.table: List[Optional[HashEntry]] = [None] * size  # Fixed-size array of HashEntry or None
        self.count = 0
        self.collision_count = 0   # Tracks total collisions for diagnostics

    def _hash(self, key: str) -> int:
        """
        Custom polynomial rolling hash function.
        Uses a prime multiplier (31) to reduce clustering compared to Python's
        built-in hash(), which can vary across interpreter runs.
        """
        hash_value = 0
        prime = 31
        for char in str(key):
            hash_value = (hash_value * prime + ord(char)) % self.size
        return hash_value

    def load_factor(self) -> float:
        """Returns the current load factor (proportion of slots filled)."""
        return self.count / self.size

    def insert(self, key, value) -> bool:
        """
        Inserts a key-value pair using linear probing.
        If the key already exists, updates its value in-place.
        Returns False if the table is full (load factor = 1.0).
        """
        if self.count == self.size:
            print("Error: Hash Table is full!")
            return False

        index = self._hash(key)

        # Probe until we find an empty slot or the same key
        while self.table[index] is not None:
            if self.table[index].key == key:
                # Key exists — update value instead of inserting duplicate
                self.table[index].value = value
                return True
            # Slot is taken by a different key — collision
            self.collision_count += 1
            index = (index + 1) % self.size  # Wrap around to slot 0 if needed

        self.table[index] = HashEntry(key, value)
        self.count += 1
        return True

    def search(self, key):
        """
        Searches for a value by key using linear probing.
        Follows the same probe sequence as insert to locate the key.
        Returns None if the key does not exist.
        """
        index = self._hash(key)
        start_index = index  # Remember where we started to detect a full loop

        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].value
            index = (index + 1) % self.size
            # Full loop completed — key is definitely not in the table
            if index == start_index:
                break

        return None

    def get_stats(self) -> dict:
        """Returns a snapshot of the table's current state for diagnostics."""
        return {
            "size": self.size,
            "occupied": self.count,
            "load_factor": f"{self.load_factor():.2%}",
            "total_collisions": self.collision_count,
        }

    def display_all(self):
        """Displays all non-empty records in a formatted table."""
        header = f"{'Bucket':<8} {'ID':<8} {'Name':<16} {'Type':<14} {'Price':>8} {'Stock':>6}"
        divider = "-" * len(header)

        print(divider)
        print(header)
        print(divider)

        found = False
        for i, entry in enumerate(self.table):
            if entry is not None:
                m = entry.value
                print(f"{i:<8} {m.product_id:<8} {m.name:<16} {m.item_type:<14} "
                      f"${m.price:>7.2f} {m.stock:>6}")
                found = True

        if not found:
            print("  The inventory is currently empty.")

        print(divider)
        stats = self.get_stats()
        print(f"  Slots used: {stats['occupied']}/{stats['size']} | "
              f"Load Factor: {stats['load_factor']} | "
              f"Total Collisions so far: {stats['total_collisions']}")
        print(divider)