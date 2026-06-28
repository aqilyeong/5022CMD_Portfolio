from typing import Callable, Optional

# ==========================================
# Merge Sort — Divide and Conquer
# ==========================================

def merge_sort(arr: list, key_func: Optional[Callable] = None,
               call_counter: Optional[list] = None) -> list:
    """
    Sorts a list using Merge Sort (Divide and Conquer).

    key_func     : Extracts the comparison key from each element.
                   Defaults to sorting Transaction objects by transaction_id.
    call_counter : Single-element list [int] passed by reference to count
                   recursive calls across all stack frames.

    Time Complexity : O(n log n) — best, average, and worst case.
    Space Complexity: O(n) — auxiliary space for merged subarrays.
    """
    if key_func is None:
        key_func = lambda x: x.transaction_id

    # Count every recursive invocation through the shared counter
    if call_counter is not None:
        call_counter[0] += 1

    # Base case: a list of 0 or 1 elements is already sorted — stop recursing
    if len(arr) <= 1:
        return arr[:]

    # ── DIVIDE ──────────────────────────────────────────────────────────────
    # Split the array into two roughly equal halves at the midpoint
    mid        = len(arr) // 2
    left_half  = arr[:mid]
    right_half = arr[mid:]

    # ── CONQUER ─────────────────────────────────────────────────────────────
    # Recursively sort each half independently until the base case is reached
    sorted_left  = merge_sort(left_half,  key_func, call_counter)
    sorted_right = merge_sort(right_half, key_func, call_counter)

    # ── COMBINE ─────────────────────────────────────────────────────────────
    # Merge the two individually sorted halves into one sorted array
    return _merge(sorted_left, sorted_right, key_func)


def _merge(left: list, right: list, key_func: Callable) -> list:
    """
    Merges two sorted lists into a single sorted list.
    Scans both halves simultaneously, always appending the smaller element first.
    """
    merged = []
    i = j  = 0

    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Only one side will have leftovers — they are already sorted, append directly
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged