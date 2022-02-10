


import hashlib
from Blockchain import Blockchain_
from Block import Block_
from Miner_Problem import miner_problem_

bc = Blockchain_(0)



class Proof_of_Work:
    def __init__(self,
        chain_id,
        txns,
        chain_data

    ) -> None:
        self.chain_id = chain_id
        self.txns = txns
        self.chain_data = chain_data

    def _proof_of_work(self, 
        previous_nonce: int, 
        index: int, 
        data: str
    ) -> int:
        new_nonce=1
        check_nonce=False
        
        while not check_nonce:
            print(new_nonce)
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
                
        return new_nonce

    def mine_block(self, chain_id:int, txns:list, chain_data:dict) -> dict:
        previous_block = bc.get_tallest_block()
        previous_nonce = previous_block['nonce']
        previous_hash = Block_.hash_block_(previous_block)
        index = len(bc.chain)
        nonce = self._proof_of_work(previous_nonce, index, chain_data)

        block = Block_(
            index = index,
            previous_hash = previous_hash,
            nonce = nonce,
            signature = "miner wallet",
            txns = self.txns,
            chain_data = self.chain_data,
            chain_id = self.chain_id
            )
        bc.append_block_(block)
        return block