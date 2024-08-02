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

  Check out the following if you are trying to see if a target value can be met.

        Both the solutions are O(m) time. The first one is if you can only use each coin ones. However, the second one is if you can use it multiple times. This is similar to the 2D array but a little different.


        # finding value tabular solution O(m) time complexity
        target = sum(stones) // 2
        cache = [0] * (target + 1)
        for stone in stones:
            for i in range(target, stone - 1,  -1): # if this is reversed, same as adding as many times as you want to
                cache[i] = max(cache[i], cache[i - stone] + stone)
        return sum(stones) - cache[-1] - cache[-1]


        """ if you can use however many """
        # cache = [0] * (amount + 1) # last one is amount
        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         cache[i] = max(cache[i], cache[i - coin] + coin)

        # if cache[-1] == amount:
        #     return 1
        # return 0

- You can only use trees with all n options when the order doen't matter. When you are restricted by the order, use only 2^n brute force optimization.
