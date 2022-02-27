# todo:
#   fix logs so they do not compound results of multiple runs

from .Proof_of_Work import Proof_of_Work, Blockchain_
import time

class Auto_Miner_:

    chain:Blockchain_
    name_:str
    wallet_:str
    def __init__(self, 
        chain:Blockchain_,
        wallet:str='_', 
        name_:str="Auto_Miner", 
        iters_:int=256, 
        quick:bool=False
    ) -> None:
        self.chain = chain
        self.wallet_ = wallet
        self.name_ = name_
        self.start_time = float
        if quick is True:
            self.iters_ = 1
        else:
            self.iters_ = iters_

    def generator(self):
        # print(self.unique_)
        self.run_timer()
        i, j = 1, self.iters_ # i is always magical
        while i <= j:
            i+=1
            proof = Proof_of_Work(self.chain, self.wallet_, '0001')
            proof.mine_block(txns={}, txn_data={})
            print(f"iter_count: {i}")

        self.end_timer()

    def run_timer(self):
        self.start_time = time.time()
        return self.start_time

    def end_timer(self):
        return round(time.time() - self.start_time, 2)

