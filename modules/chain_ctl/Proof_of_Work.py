


import hashlib, time, os, json, datetime
from random import randint
from .Blockchain import Blockchain_, Block_
from .Miner_Problem import miner_problem_

class Timer:
    def __init__(self) -> None:
        self.start_time = float
    def start_timer(self):
        self.start_time = time.time()
        return self.start_time
    def end_timer(self):
        return round(time.time() - self.start_time, 2)
TIMER = Timer()
class Proof_of_Work:
    def __init__(self,
        chain_:Blockchain_,
        txns=[],
        chain_data={}

    ) -> None:
        
        self.chain_ = chain_
        self.chain_id = self.chain_.chain_id
        self.txns = txns
        self.chain_data = chain_data

    def proof_of_work_(self, 
        previous_nonce: int, 
        index: int, 
        data: str,
    ) -> int:
        new_nonce=1
        check_nonce=False
        TIMER.start_timer()
        while not check_nonce:
            # print(new_nonce)
            hash_digest = miner_problem_(
                new_nonce=new_nonce, 
                previous_nonce=previous_nonce, 
                index=index, 
                data=data
            )
            hash_value = hashlib.sha256(hash_digest).hexdigest()

            # increase nonce hash difficulty exponentionally
            # checking how many 0s must be found at start 
            if hash_value[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        print("MINE_TIME: ", TIMER.end_timer(), "sec")
        try:
            with open(f'{os.getcwd()}/minter_data/Block_times.txt', 'x') as file:
                list_ = [
                    str(datetime.datetime.now()),
                    self.chain_data,
                    self.txns,
                    {"previous_hash": self.chain_.get_tallest_block()[1]},
                    {"previous_block": self.chain_.get_tallest_block()[0]}
                    
                ]
                # for i in file_:
                    # list_.append(i)
                list_.append(str("time: " + str(TIMER.end_timer()) + "sec"))
                file.write((json.dumps(list_, indent=2)))                
                # file.write(json.dumps([{"Chain": "Data"}, ["Txns"], "Time in seconds"], indent=2))
        except FileExistsError:
            with open(f'{os.getcwd()}/minter_data/Block_times.txt', 'a+') as file:
                # file_ = dict(json.load(file))
                list_ = [
                    str(datetime.datetime.now()),
                    self.chain_data,
                    self.txns,
                    {"previous_hash": self.chain_.get_tallest_block()[1]},
                    {"previous_block": self.chain_.get_tallest_block()[0]}

                ]
                # for i in file_:
                    # list_.append(i)
                list_.append(str("time(sec): " + str(TIMER.end_timer())))
                list_.append(str("time(min): " + str(round(TIMER.end_timer() // 60, 2))))
                file.write((json.dumps(list_, indent=2)))

        return new_nonce

    def mine_block(self, txns:list=[], chain_data:dict={}) -> dict:
        previous_block = self.chain_.get_tallest_block()[0]
        previous_nonce = previous_block['nonce']
        mock = Block_(
            index = 0,
            previous_hash = "",
            nonce = previous_nonce * 3,
            signature = f"MOCK_BLOCK_{randint(0, 69420)}",
            txns = [],
            chain_data = [],
            )
        previous_hash = mock.hash_block_(previous_block)
        index = len(self.chain_.chain)
        nonce = self.proof_of_work_(previous_nonce, index, str(mock))

        block = Block_(
            index = index,
            previous_hash = previous_hash,
            nonce = nonce,
            signature = "miner wallet",
            txns = self.txns,
            chain_data = self.chain_data,
            chain_id = self.chain_id,
            print_it = True
            )
        self.chain_.append_block_(block)
        return block