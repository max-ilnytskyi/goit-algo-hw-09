import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


coins = [50, 25, 10, 5, 2, 1]


@timer
def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= count * coin
    return result


@timer
def find_min_coins(amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    used_coins = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = coin

    result = {}
    while amount > 0:
        coin = used_coins[amount]
        result[coin] = result.get(coin, 0) + 1

        amount -= coin

    return result


amount = 11300

print(f"Find coins greedy result: {find_coins_greedy(amount)}")
print(f"Find min coins result: {find_min_coins(amount)}")
