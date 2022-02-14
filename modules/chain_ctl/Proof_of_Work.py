


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
        self.difficulty = int

    def proof_of_work_(self, 
        previous_nonce: int, 
        index: int, 
        data: str,
    ) -> int:
        new_nonce=1
        check_nonce=False
        TIMER.start_timer()
        print(f"Timer started::fishing block: {len(self.chain_.chain) - 1} -> chain_height: {len(self.chain_.chain)}")

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
            if len(self.chain_.chain) == 1:
                self.difficulty = 0
                check_nonce = True        
            elif len(self.chain_.chain) < 100:
                self.difficulty = 1
                if hash_value[:1] == '0':
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 105:
                self.difficulty = 2
                if hash_value[:2] == '00':
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 750:
                self.difficulty = 3
                if hash_value[:3] == '000':
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 1000:
                self.difficulty = 4
                if hash_value[:4] == '0000':
                    check_nonce = True
                else:
                    new_nonce += 1                
            elif len(self.chain_.chain) < 7500:
                self.difficulty = 5
                if hash_value[:5] == '00001':
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 10000:
                self.difficulty = 6
                if hash_value[:6] == '000013':
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 15000:
                self.difficulty = 7
                if hash_value[:7] == '0000133':
                    check_nonce = True
                else:
                    new_nonce += 1
            elif len(self.chain_.chain) < 2000:
                self.difficulty = 8
                if hash_value[:8] == '00001337':
                    check_nonce = True
                else:
                    new_nonce += 1
            else:
                self.difficulty = 9
                if 'hellofromdanmuck' in hash_value[:]:
                    check_nonce = True
                else:
                    new_nonce += 1
        print("MINE_TIME:", round(TIMER.end_timer(), 8), "sec")
        print("MINE_TIME:", f"{round(TIMER.end_timer() // 60, 8)}ish min")
        try:
            with open(f'{os.getcwd()}/chain_data/Block_times_{self.chain_id}.txt', 'x') as file:
                file.write(f"{str(TIMER.end_timer())}s\t\t: {self.difficulty}\n")               
        except FileExistsError:
            with open(f'{os.getcwd()}/chain_data/Block_times_{self.chain_id}.txt', 'a+') as file:
                file.write(f"{str(TIMER.end_timer())}s\t\t: {self.difficulty}\n")

        return new_nonce

    def mine_block(self, txns:list=[], chain_data:dict={}) -> dict:
        self.chain_.update_chain_data_()
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





