from typing import Optional, Tuple
from Q2_Transaction import Transaction

# ==========================================
# Binary Search — Divide and Conquer
# ==========================================

def binary_search(arr: list, target_id: str) -> Tuple[Optional[Transaction], int]:
    """
    Searches for a Transaction by ID using Binary Search (Divide and Conquer).

    PRE-CONDITION: arr must be sorted by transaction_id ascending.
    Returns: (Transaction or None, number of comparisons made)

    Time Complexity: O(log n) average/worst case; O(1) best case.
    """
    low         = 0
    high        = len(arr) - 1
    comparisons = 0
    target_id   = target_id.strip().upper()

    while low <= high:
        # ── DIVIDE: compute the midpoint of the current search range ─────────
        mid    = (low + high) // 2
        mid_id = arr[mid].transaction_id
        comparisons += 1

        # ── CONQUER: determine which half to search next ─────────────────────
        if mid_id == target_id:
            return arr[mid], comparisons       # Found
        elif mid_id < target_id:
            low = mid + 1                      # Target is in the right half
        else:
            high = mid - 1                     # Target is in the left half

    # ── COMBINE: search range exhausted — target does not exist ─────────────
    return None, comparisons


# ==========================================
# Linear Search — Sequential (for comparison)
# ==========================================

def linear_search(arr: list, target_id: str) -> Tuple[Optional[Transaction], int]:
    """
    Searches for a Transaction by ID using Linear Search.
    Scans every element sequentially — O(n) time.
    Used as a performance baseline against Binary Search.

    Returns: (Transaction or None, number of comparisons made)
    """
    comparisons = 0
    target_id   = target_id.strip().upper()

    for item in arr:
        comparisons += 1
        if item.transaction_id == target_id:
            return item, comparisons

    return None, comparisons