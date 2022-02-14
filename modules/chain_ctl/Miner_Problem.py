



from os import system
from random import randint
import time, hashlib, platform

from multiprocessing import Pool


def arb_tasks(switch:int):
    if switch == 0:
        return str((randint(123, 999) ** 5) + randint(321, 9999) ** 3 + time.time_ns())  
    elif switch == 1:
        return str((randint(234, 999) ** 6) + randint(432, 9999) ** 5 + time.time_ns())  
    elif switch == 2:
        return str((randint(345, 9999) ** 7) + randint(543, 9999) ** 7 + time.time_ns())  
    elif switch == 3:
        return str((randint(4567, 99999) ** 8) + randint(654, 9999) ** 9 + time.time_ns())  
    elif switch == 4:
        return str((randint(5678, 999999) ** 9) + randint(765, 9999) ** 11 + time.time_ns())  
    elif switch == 5:
        return str((randint(6789, 9999999) ** 10) + randint(876, 9999) ** 13 + time.time_ns())  
    elif switch == 6:
        return str((randint(7890, 9999999) ** 11) + randint(987, 99999) ** 15 + time.time_ns())  
    elif switch == 7:
        return str((randint(8901, 9999999) ** 12) + randint(9876, 999999) ** 17 + time.time_ns())  
    elif switch == 8:
        return str((randint(9012, 9999999) ** 13) + randint(8765, 9999999) ** 19 + time.time_ns())  
    elif switch == 9:
        return str((randint(12343, 99999) ** 14) + randint(7654, 9999999) ** 21 + time.time_ns())  
    elif switch == 10:
        return str((randint(23454, 9999) ** 15) + randint(6543, 99999999) ** 23 + time.time_ns())  
    elif switch == 11:
        return str((randint(34565, 99999) ** 16) + randint(5432, 99999999) ** 25 + time.time_ns())  
    elif switch == 12:
        return str((randint(45676, 999999) ** 17) + randint(4321, 99999999) ** 27 + time.time_ns())  
    elif switch == 13:
        return str((randint(56787, 9999999) ** 18) + randint(3211, 99999999) ** 29 + time.time_ns())  
    elif switch == 14:
        return str((randint(67898, 99999999) ** 19) + randint(2111, 99999999) ** 31 + time.time_ns())       
    elif switch == 15:
        return str((randint(78909, 999999999) ** 33) + randint(1111, 99999999) ** 33 + time.time_ns())  
    else:
        return str((time.time_ns() + randint(9, 999) ** 3))     

def arb_tasks_testing(switch:int):
    task = str
    if switch == 0:
        task = str((time.time_ns() ** 3) // (randint(69, time.time_ns() + randint(13, 333))))
        return hashlib.sha512(task.encode()).hexdigest()
    elif switch == 1:
        task = str((time.time_ns() ** 7) // (randint(69, time.time_ns() + randint(13, 777))))
        return hashlib.sha512(task.encode()).hexdigest()
    else:
        return str((time.time_ns() ** 3) // (randint(3, time.time_ns() + randint(3, 6))))

def start_work() -> str:
    with Pool() as p:
        try:
            process_map = p.map(arb_tasks, [0, 1, 2, 3, 4, 5, 6, 7])
            process_map_2 = p.map(arb_tasks_testing, [0, 1, 0 , 1])
            # encode_it = ''.join(process_map)
            maps_ = []
            maps_.extend(process_map)
            maps_.extend(process_map_2)
            encode_it = ''.join(maps_)
            return encode_it
        except:
            p.close()
            p.terminate()
        finally:
            p.close()
            p.terminate()   

def start_single_work() -> str:
    task_1 = arb_tasks(99)
    task_2 = arb_tasks_testing(99)
    encode_it = ''.join([task_1, task_2])
    return encode_it

def miner_problem_(new_nonce: int, previous_nonce: int, index: str, data: str) -> bytes:
    miner_problem = str(new_nonce ** 2 - previous_nonce ** 2 + index) + data
    single_problem = start_single_work()
    if "macOS" in platform.platform() or "Windows" in platform.platform():
        other_problem = str(((randint(77, 1333) ** randint(77, 711)) * randint(137, 555) ** randint(777, 7711)) // randint(1337, 9999))
        miner_problem = str(((randint(133, 711) ** randint(133, 711)) * randint(133, 555) ** randint(133, 711)) // randint(1337, 9999))

    else:
        other_problem = start_work()

    problems = [miner_problem, single_problem, other_problem]
    encode_it = ''.join(problems)

    return encode_it.encode()
