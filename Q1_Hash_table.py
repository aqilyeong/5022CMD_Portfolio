class HashEntry:
    """Stores the key-value pair for the Hash Table."""

    def __init__(self, key, value):
        self.key = key
        self.value = value


class LinearProbeHashTable:
    """Hash Table using Linear Probing for collision resolution."""

    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def _hash(self, key):
        """Simple modulo hash function based on the string or integer key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Inserts a key-value pair using linear probing."""
        if self.count == self.size:
            print("Error: Hash Table is full!")
            return False

        index = self._hash(key)

        # Linear Probing: Find next available slot
        while self.table[index] is not None:
            # Update if key already exists
            if self.table[index].key == key:
                self.table[index].value = value
                return True
            index = (index + 1) % self.size  # Wrap around

        self.table[index] = HashEntry(key, value)
        self.count += 1
        return True

    def search(self, key):
        """Searches for a value by key using linear probing."""
        index = self._hash(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].value
            index = (index + 1) % self.size
            # Stop if we have checked every slot
            if index == start_index:
                break

        return None  # Key not found

    def display_all(self):
        """Displays all non-empty records in the hash table."""
        print("-" * 50)
        found = False
        for i, entry in enumerate(self.table):
            if entry is not None:
                print(f"Bucket {i}: {entry.value}")
                found = True
        if not found:
            print("The inventory is empty.")
        print("-" * 50)