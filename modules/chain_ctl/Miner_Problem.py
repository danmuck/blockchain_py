




from random import randint
import time


def miner_problem_(new_nonce: int, previous_nonce: int, index: str, data: str) -> bytes:
    # make more difficult
    miner_problem = str(new_nonce ** 2 - previous_nonce ** 2 + index) + data
    expo_problem = str(randint(0, 99) % 3 + randint(1, 768) + time.time_ns())
    mean_problem = str((time.time_ns() ** 555) % randint(0, time.time_ns()))
    problems = [miner_problem, expo_problem, mean_problem]
    encode_it = ''.join(problems)

    return encode_it.encode()