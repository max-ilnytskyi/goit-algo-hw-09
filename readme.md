# Homework #9: Greedy Algorithms and Dynamic Programming

## Introduction

This homework assignment focuses on the implementation of two fundamental optimization techniques in algorithm analysis: **Greedy Algorithms** and **Dynamic Programming**. The aim is to explore how these algorithms can be applied to solve the coin change problem, comparing their performance, time complexity, and efficiency in generating the desired results.

## Implementation Details

### Greedy Algorithm (`find_coins_greedy`)

The greedy approach iterates through the list of coin denominations, starting from the highest value, and uses as many of that coin as possible before moving to the next smaller denomination. This approach may not always provide the minimum number of coins but is often faster and simpler.

- **Time Complexity**: O(n), where n is the number of coin denominations.
- **Optimality**: Not guaranteed for all cases but works correctly with the given coin set.

### Dynamic Programming (`find_min_coins`)

The dynamic programming approach builds an array that tracks the minimum number of coins required for each amount from 0 to the target amount. It ensures the minimum number of coins is used, making it an optimal solution for this problem.

- **Time Complexity**: O(m * n), where m is the target amount and n is the number of coin denominations.
- **Optimality**: Guaranteed to provide the minimum number of coins for any coin set.

## Results

Based on the execution of the algorithms with the test amount of **11300**, the following results were observed:

1. **Greedy Algorithm**
   - Execution Time: 0.000000 seconds
   - Result: `{50: 226}`
   - The greedy algorithm provided the change using 226 coins of the highest denomination, achieving the target amount quickly but without considering potential combinations with fewer total coins.

2. **Dynamic Programming**
   - Execution Time: 0.007988 seconds
   - Result: `{50: 226}`
   - The dynamic programming algorithm also resulted in 226 coins of denomination 50, which matches the greedy solution in this specific case due to the nature of the coin set.

## Analysis

### Performance
- The **greedy algorithm** has a faster execution time due to its straightforward iteration and selection of the largest denomination first.
- The **dynamic programming algorithm** takes longer to execute due to its iterative nature and the construction of the `dp` array, which tracks the minimum coin counts for each amount up to the target.

### Efficiency
- While both algorithms resulted in the same number of coins for the given test amount, this may not always be the case with different coin sets. The **dynamic programming approach** is more reliable for ensuring the minimum number of coins in general.
- For large amounts, the **greedy algorithm** remains faster but potentially less accurate in cases where smaller denominations could reduce the total number of coins used.

## Conclusion

- The **greedy algorithm** is more suitable for situations where speed is critical and the coin set is known to work well with a greedy approach.
- The **dynamic programming algorithm** is preferable when optimality is crucial, as it ensures the minimum number of coins is used.

This comparison illustrates the trade-off between speed and optimality, emphasizing the importance of understanding the problem requirements when choosing an algorithmic approach.
