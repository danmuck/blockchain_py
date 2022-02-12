




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
    task = str
    if switch == 0:
        task = str(randint(0, 999) % 3 + randint(1, 768) + time.time_ns())
        return task
    elif switch == 1:
        task = str(randint(0, 199) % 6 + randint(768, 1024) + time.time_ns())
        return task
    elif switch == 2:
        task = str((time.time_ns() ** 32) // (randint(0, time.time_ns() + randint(1, 3))))
        return task
    elif switch == 3:
        task = str((time.time_ns() ** 12) // (randint(0, time.time_ns() + randint(3, 6))))
        return task
    elif switch == 4:
        task = str(randint(0, 199) % 2 + randint(7, 10) + time.time_ns())
        return task
    elif switch == 5:
        task = str((time.time_ns() ** 3) // (randint(0, time.time_ns() + randint(1, 3))))
        return task
    elif switch == 6:
        task = str((time.time_ns() ** 2) // (randint(0, time.time_ns() + randint(3, 6))))
        return task
    else:
        pass

def start_work() -> str:

    with Pool() as p:
        try:
            process_map = p.map(arb_tasks, [0, 1, 2, 3, 4, 5, 6])
            # process_map_2 = p.map(arb_tasks_testing, [0, 1, 2, 3])
            # encode_it = ''.join(process_map_2)

            # print(process_map)
            encode_it = ''.join(process_map)
            p.close()
            p.terminate()
            return encode_it
        except KeyboardInterrupt:
            p.close()
            p.terminate()
        

def miner_problem_(new_nonce: int, previous_nonce: int, index: str, data: str) -> bytes:
    # make more difficult
    miner_problem = str(new_nonce ** 2 - previous_nonce ** 2 + index) + data
    other_problem = start_work()
    problems = [miner_problem, other_problem]
    encode_it = ''.join(problems)

    return encode_it.encode()
