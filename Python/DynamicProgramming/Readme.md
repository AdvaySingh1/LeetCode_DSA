For Dynamic programming questions

Type One: Equaling a certain value: (Target value, partition in half).

- Brute force O(2^n) solution with O(n) time.
- Memoization O(n \* m) solution where m is the total things can be (time and space).
- Tabular O(n \* m) solution where m is the total things can be (time and space).
  - Usually a set or list which grows everytime
  - There can be an O(m) space solution (see splitting rocks for example).

Type Two: Max calue: (Knapsack, 1s and 0s).

- Brute force O(2^n) solution with O(n) time.
- Memoization O(n \* m) solution where m is the total things can be (time and space).
- Tabular O(n \* m) solution where m is the total things can be (time and space).
  - Usually a multi dimensional cache where the values depend on the previous n and m in the cache
  - Can be optimized to O(m) space.
