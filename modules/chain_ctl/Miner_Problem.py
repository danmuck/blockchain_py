



from random import randint
import time, hashlib

from multiprocessing import Pool


def arb_tasks(switch:int):
    if switch == 0:
        return str(randint(0, 99999) % 3 + randint(1, 768) + time.time_ns())
    elif switch == 1:
        return str(randint(0, 19999) % 6 + randint(768, 1024) + time.time_ns())
    elif switch == 2:
        return str((time.time_ns() ** 32) // (randint(0, time.time_ns() + randint(1, 3))))
    elif switch == 3:
        return str((time.time_ns() ** 35) // (randint(0, time.time_ns() + randint(3, 6))))
    elif switch == 4:
        return str(randint(555, 9999999) % 55 + randint(7, 10) + time.time_ns() ** 35)
    elif switch == 5:
        return str((time.time_ns() ** 3) // (randint(0, time.time_ns() + randint(1, 3))))
    elif switch == 6:
        return str((time.time_ns() ** 2) // (randint(0, time.time_ns() + randint(3, 6))))
    elif switch == 7:
        return str(((randint(0, 99999999) % 7 + randint(7, 10480) * (time.time_ns() ** 5)) * (randint(0, time.time_ns() + randint(3, 666)))))        
    elif switch == 8:
        return str((randint(69, 42069) // 3) + randint(777, 69420) ** 3 + time.time_ns())
    elif switch == 9:
        return str((time.time_ns() ** 33) // (randint(0, time.time_ns() + randint(1, 3333))))
    elif switch == 10:
        return str((time.time_ns() ** 7) // (randint(0, time.time_ns() + randint(3, 64))))    
    elif switch == 11:
        return str(randint(555555, 9999999) % 55 + randint(7, 10) + time.time_ns() ** 35)
    elif switch == 12:
        return str((time.time_ns() ** 3) // (randint(0, time.time_ns() + randint(1, 3))))
    elif switch == 13:
        return str((time.time_ns() ** 2) // (randint(0, time.time_ns() + randint(3, 6))))
    elif switch == 14:
        return str(((randint(444444, 99999999) % 7 + randint(7, 10480) * (time.time_ns() ** 5)) * (randint(0, time.time_ns() + randint(333, 666)))))        
    elif switch == 15:
        return str((randint(696969, 4204206969) ** 3) + randint(777, 69420) ** 3 + time.time_ns())  
    else:
        return str((time.time_ns() + randint(9, 999) ** 13) // (randint(0, time.time_ns() + randint(3, 6))))        

def arb_tasks_testing(switch:int):
    task = str
    if switch == 0:
        task = str(randint(0, 999) ** 39 + randint(1, 768) + time.time_ns())
        hash_value = hashlib.sha256(task.encode()).hexdigest()
        return hash_value
    elif switch == 1:
        task = str(randint(0, 199) ** 69 + randint(768, 1024) + time.time_ns())
        hash_value = hashlib.sha256(task.encode()).hexdigest()
        return hash_value
    elif switch == 2:
        task = str((time.time_ns() ** 32) // (randint(0, time.time_ns() + randint(1, 3))))
        hash_value = hashlib.sha256(task.encode()).hexdigest()
        return hash_value
    elif switch == 3:
        task = str((time.time_ns() ** 12) // (randint(0, time.time_ns() + randint(3, 6))))
        hash_value = hashlib.sha256(task.encode()).hexdigest()
        return hash_value
    elif switch == 4:
        task = str(randint(0, 199) ** 29 + randint(7, 10) + time.time_ns())
        hash_value = hashlib.sha256(task.encode()).hexdigest()
        return hash_value
    elif switch == 5:
        task = str((time.time_ns() ** 3) // (randint(0, time.time_ns() + randint(1, 3))))
        hash_value = hashlib.sha256(task.encode()).hexdigest()
        return hash_value
    elif switch == 6:
        task = str((time.time_ns() ** 23) // (randint(0, time.time_ns() + randint(3, 6))))
        hash_value = hashlib.sha256(task.encode()).hexdigest()
        return hash_value
    elif switch == 7:
        task = str((time.time_ns() ** 22) // (randint(0, time.time_ns() + randint(3, 6))))
        hash_value = hashlib.sha256(task.encode()).hexdigest()
        return hash_value
    else:
        task = str((time.time_ns() ** 77) // (randint(0, time.time_ns() + randint(3, 6))))
        hash_value = hashlib.sha256(task.encode()).hexdigest()
        return hash_value

def start_work() -> str:
    with Pool() as p:
        try:
            process_map = p.map(arb_tasks, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
            process_map_2 = p.map(arb_tasks_testing, [0, 1, 2, 3, 4, 5, 6, 7])
            # encode_it = ''.join(process_map)
            maps_ = []
            maps_.extend(process_map)
            maps_.extend(process_map_2)
            encode_it = ''.join(maps_)

            p.close()
            p.terminate()
            return encode_it
        except:
            p.close()
            p.terminate()


def miner_problem_(new_nonce: int, previous_nonce: int, index: str, data: str) -> bytes:
    # make more difficult
    miner_problem = str(new_nonce ** 2 - previous_nonce ** 2 + index) + data
    other_problem = start_work()
    problems = [miner_problem, other_problem]
    encode_it = ''.join(problems)

    return encode_it.encode()
