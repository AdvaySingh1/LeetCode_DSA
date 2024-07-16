

"""
 * The following impl is also the same time and space complexity as the recursive iteration (O(n) space and O(n) time (prove using divide and conquer strong induction)).
 * Difference from the normal recursive implementation: we have our own cute lil stack.
 *
 * Space is theta(log n) and O(n) no omega.
 * What to prove: T(n) = T(k) + T(n-k-1) + O(1) = O(n) (omega in this case).
 """