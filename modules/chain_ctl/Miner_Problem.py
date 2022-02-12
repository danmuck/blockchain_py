




from random import randint
import time

from multiprocessing import Pool


def arb_tasks(switch:int):
    if switch == 0:
        return str(randint(0, 99999) % 3 + randint(1, 768) + time.time_ns())
    elif switch == 1:
        return str(randint(0, 19999) % 6 + randint(768, 1024) + time.time_ns())
    elif switch == 2:
        return str((time.time_ns() ** 32) // (randint(0, time.time_ns() + randint(1, 3))))
    elif switch == 3:
        return str((time.time_ns() ** 12) // (randint(0, time.time_ns() + randint(3, 6))))
    elif switch == 4:
        return str(randint(0, 199) % 2 + randint(7, 10) + time.time_ns())
    elif switch == 5:
        return str((time.time_ns() ** 3) // (randint(0, time.time_ns() + randint(1, 3))))
    elif switch == 6:
        return str((time.time_ns() ** 2) // (randint(0, time.time_ns() + randint(3, 6))))
    else:
        pass

def arb_tasks_testing(switch:int):
    if switch == 0:
        return str(randint(0, 999) % 3 + randint(1, 768) + time.time_ns())
    elif switch == 1:
        return str(randint(0, 199) % 6 + randint(768, 1024) + time.time_ns())
    elif switch == 2:
        return str((time.time_ns() ** 32) // (randint(0, time.time_ns() + randint(1, 3))))
    elif switch == 3:
        return str((time.time_ns() ** 12) // (randint(0, time.time_ns() + randint(3, 6))))
    elif switch == 4:
        return str(randint(0, 199) % 2 + randint(7, 10) + time.time_ns())
    elif switch == 5:
        return str((time.time_ns() ** 3) // (randint(0, time.time_ns() + randint(1, 3))))
    elif switch == 6:
        return str((time.time_ns() ** 2) // (randint(0, time.time_ns() + randint(3, 6))))
    else:
        pass

def start_work() -> str:
    with Pool() as p:
        # process_map = p.map(arb_tasks, [0, 1, 2, 3, 4, 5, 6])
        process_map_2 = p.map(arb_tasks_testing, [0, 1, 2, 3, 4, 5, 6])

        # print(process_map)
        # encode_it = ''.join(process_map)
        encode_it = ''.join(process_map_2)
        p.close()
        p.terminate()
        return encode_it

def miner_problem_(new_nonce: int, previous_nonce: int, index: str, data: str) -> bytes:
    # make more difficult
    miner_problem = str(new_nonce ** 2 - previous_nonce ** 2 + index) + data
    other_problem = start_work()
    problems = [miner_problem, other_problem]
    encode_it = ''.join(problems)

    return encode_it.encode()
