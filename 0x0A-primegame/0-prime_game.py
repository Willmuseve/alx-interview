#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    """
    Returns name of the winner
    """

    if not nums or x < 1:
        return None

    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    prime_indices = [i for i, value in enumerate(is_prime) if value]

    maria_wins = sum(
        1 for num in nums if num < len(prime_indices) \
            and prime_indices[num] % 2 == 1
    )

    if maria_wins * 2 == len(nums):
        return None
    elif maria_wins * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
