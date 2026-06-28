# ==========================================
# Factorial Function (Q3 #2)
# ==========================================

def factorial(n: int) -> int:
    """
    Iteratively computes n! (n factorial).

    --- Primitive Operation Count (for Big-O derivation) ---
      result = 1                  -> 1 assignment           (constant)
      for i in range(2, n + 1):   -> loop runs (n - 1) times
          result *= i             -> 1 multiplication + 1 assignment per pass
      return result               -> 1 return               (constant)

    Total operations ≈ 2(n - 1) + 2  =  2n
    Dropping constants and coefficients -> the work scales linearly with n.

    Time Complexity : O(n)
        (each loop pass is counted as a primitive operation; the number of
         passes is directly proportional to the input size n)
    Space Complexity: O(1)
        (a single accumulator variable is reused; no extra storage grows with n)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1                      # base case: 0! = 1! = 1
    for i in range(2, n + 1):       # multiply successively: 2 * 3 * ... * n
        result *= i
    return result