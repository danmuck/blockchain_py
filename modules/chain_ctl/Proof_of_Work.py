


import hashlib
from .Blockchain import Blockchain_
from .Block import Block_
from .Miner_Problem import miner_problem_



class Proof_of_Work:
    def __init__(self,
        chain_id=0,
        txns=[],
        chain_data={}

    ) -> None:
        self.chain_id = chain_id
        self.txns = txns
        self.chain_data = chain_data

    def proof_of_work_(self, 
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

    def mine_block(self, chain:Blockchain_, txns:list=[], chain_data:dict={}, chain_id:int=0) -> dict:
        previous_block = chain.get_tallest_block()[0]
        previous_nonce = previous_block['nonce']
        mock = Block_(
            index = 0,
            previous_hash = "",
            nonce = 0,
            signature = "MOCK_BLOCK",
            txns = [],
            chain_data = [],
            chain_id = 0
            )
        previous_hash = mock.hash_block_(previous_block)
        index = len(chain.chain)
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
        chain.append_block_(block)
        return block