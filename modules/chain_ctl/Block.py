import datetime, json, hashlib


class Block_:
    def __init__(self,
        index: int,
        previous_hash: str,
        nonce: int,
        txns: list,
        signature: str,
        chain_data: dict,
        chain_id:int=0,
    ) -> None:
        self.block = {
            'index': index,
            'time': str(datetime.datetime.now()),
            'signature': signature,
            'chain_data': chain_data,
            'transactions': txns,
            'nonce': nonce,
            'previous_hash': previous_hash
            } 

        self.block_hash = self.hash_block_(self.block)
        self.block_dict = {self.block_hash: self.block}
        print("\n\nNew Block_ initialized... \nBLOCK: ", json.dumps(self.block, indent=2))
        print("BLOCK_HASH: ", self.block_hash)
        print("PREV_HASH:  ",self.block['previous_hash'])

    def hash_block_(self, block:dict) -> str:
        '''
        Hash a block and return the cryptographic hash value of the block

        convert a string -> bytes and return encrypted hash
        '''
        
        encoded_block = json.dumps(block).encode()
        return ''.join(('0x', hashlib.sha256(encoded_block).hexdigest()))
        