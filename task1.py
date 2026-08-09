import timeit

COIN_DENOMINATIONS = [50, 25, 10, 5, 2, 1]
MEASUREMENTS = 100

def measure_time(find_coin_function, sum):
    total_time = timeit.timeit(
        lambda: find_coin_function(sum),
        number=MEASUREMENTS,
    )

    return total_time / MEASUREMENTS

def find_coins_greedy(sum):
    coins_dictionary = {}
    for denomination in COIN_DENOMINATIONS:
        if sum == 0:
            break
        number_of_coins = sum // denomination
        if number_of_coins > 0:
            coins_dictionary[denomination] = number_of_coins
            sum -= denomination * number_of_coins
    return coins_dictionary

def find_min_coins(sum):
    min_coins_required = [0] + [float('inf')] * sum
    last_coin_used = [0] * (sum + 1)
    
    for current_sum in range(1, sum + 1):
        for denomination in sorted(COIN_DENOMINATIONS):
            if denomination <= current_sum:
                candidate = min_coins_required[current_sum - denomination] + 1
                if candidate < min_coins_required[current_sum]:
                    min_coins_required[current_sum] = candidate
                    last_coin_used[current_sum] = denomination
                    
    result = {}
    
    while sum > 0:
        denomination = last_coin_used[sum]
        result[denomination] = result.get(denomination, 0) + 1
        sum -= denomination
        
    return result

def measure_algorithms(sums = [100, 1_000, 10_000, 100_000, 1_000_000]):
    print(f"{'Sum':<20}{'Greedy (s)':<20}{'DP (s)':<20}")
    
    for sum in sums:
        greedy_time = measure_time(find_coins_greedy, sum)
        dp_time = measure_time(find_min_coins, sum)
        print(f"{sum:<20}{greedy_time:<20.9f}{dp_time:<20.9f}")
    
def main():
    sum = int(input('Enter the sum'))
    print('Greedy Algorithm')
    print(find_coins_greedy(sum))
    print('Dynamic Programming Algorithm')
    print(find_min_coins(sum))
    
    measure_algorithms()    

if __name__ == "__main__":
    main()
