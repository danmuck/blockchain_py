




from random import randint
import time

from multiprocessing import Pool


def prob_0(switch:int):
    if switch == 0:
        return str(randint(0, 99) % 3 + randint(1, 768) + time.time_ns())
    elif switch == 1:
        return str(randint(0, 199) % 6 + randint(768, 1024) + time.time_ns())
    elif switch == 2:
        return str((time.time_ns() ** 666) // (randint(0, time.time_ns() + randint(1, 3))))
    elif switch == 3:
        return str((time.time_ns() ** 333) // (randint(0, time.time_ns() + randint(3, 6))))
    else:
        pass

def start_work() -> str:
    with Pool(4) as p:
        process_map = p.map(prob_0, [0, 1, 2, 3])
        # print(process_map)
        encode_it = ''.join(process_map)
        return encode_it

def miner_problem_(new_nonce: int, previous_nonce: int, index: str, data: str) -> bytes:
    # make more difficult
    miner_problem = str(new_nonce ** 2 - previous_nonce ** 2 + index) + data
    other_problem = start_work()
    problems = [miner_problem, other_problem]
    encode_it = ''.join(problems)

    return encode_it.encode()
